
from architecture.View import View
from architecture.event.Event import Event

import tkinter as tk
from abc import abstractmethod


class InteractiveCanvas(View):

    selection_search_radius: int = 5

    class CanvasElement:

        __id_counter: int = 0

        def __init__(self) -> None:
            
            self.__id: int = self.__class__.__id_counter
            self.__class__.__id_counter += 1

        @property
        def id(self) -> int:
            return self.__id

        @abstractmethod
        def draw(self, context: tk.Canvas) -> int:
            pass

    def __init__(self, master: tk.Tk | tk.Toplevel | tk.Frame) -> None:
        View.__init__(self, master=master)

        self.__canvas: tk.Canvas = tk.Canvas(master=self.frame)
        self.__canvas.pack(expand=True, fill=tk.BOTH)

        self.__canvas.config(
            background='grey',
            cursor='crosshair'
        )

        self.__running: bool = False
        self.__update_delay: int = 33
        self.__issue_update_events: bool = False

        self.__cursor_x: int = None
        self.__cursor_y: int = None

        self.__elements: dict[int, InteractiveCanvas.CanvasElement] = {}

        self.__element_id_volatile_id_lookup_table: dict[int, int] = {}
        self.__element_volatile_id_id_lookup_table: dict[int, int] = {}

        self.__focused_element_id: int = None
        self.__element_ids_scheduled_for_update: set[int] = set()

        self.Binding(context=self.__canvas, identifier='CanvasMotion', sequence='<Motion>', func=self.__motion)
        self.Binding(context=self.__canvas, identifier='CanvasLeftClick', sequence='<Button-1>', func=self.__left_click)
        self.Binding(context=self.__canvas, identifier='CanvasRightClick', sequence='<Button-3>', func=self.__right_click)

        self._dynamic_binding_list = ['CanvasMotion', 'CanvasLeftClick', 'CanvasRightClick']

    @property
    def cursor_position(self) -> tuple[int, int]:
        return (self.__cursor_x, self.__cursor_y)

    def issue_update_events(self) -> None:
        self.__issue_update_events = True

    def new_element(self, element: 'InteractiveCanvas.CanvasElement') -> None:
        self.__elements[element.id] = element

    def schedule_element_update(self, element_id: int) -> None:
        self.__element_ids_scheduled_for_update.add(element_id)

    def _enter(self, _: tk.Event) -> None: # override
        self.__run()

    def _leave(self, _: tk.Event) -> None: # override
        self.__stop()

    def __run(self) -> None:

        self.__running = True
        self.frame.winfo_toplevel().after(self.__update_delay, self.__update)
        
    def __stop(self) -> None:
        self.__running = False

    def __update(self) -> None:

        self.__update_focused_element_id()
        self.__update_elements()

        if self.__issue_update_events:

            self.event_dispatcher.schedule_event_for_dispatch(
                event=Event(
                    trigger='UpdateEvent'
                )
            )

        self.event_dispatcher.dispatch_scheduled_events()

        if self.__running:
            self.frame.winfo_toplevel().after(self.__update_delay, self.__update)

    def __update_elements(self) -> None:

        for element_id in self.__element_ids_scheduled_for_update:

            element: InteractiveCanvas.CanvasElement = self.__elements[element_id]

            try:
                volatile_id: int = self.__element_id_volatile_id_lookup_table[element_id]
                self.__canvas.delete(volatile_id)
                del self.__element_volatile_id_id_lookup_table[volatile_id]
            except KeyError:
                pass

            volatile_id: int = element.draw(context=self.__canvas)

            self.__element_id_volatile_id_lookup_table[element_id] = volatile_id
            self.__element_volatile_id_id_lookup_table[volatile_id] = element_id

        self.__element_ids_scheduled_for_update.clear()

    def __update_focused_element_id(self) -> None:

        overlapping_element_volatile_ids: tuple[int] = self.__canvas.find_overlapping(
            x1=self.__cursor_x - self.__class__.selection_search_radius, 
            y1=self.__cursor_y - self.__class__.selection_search_radius, 
            x2=self.__cursor_x + self.__class__.selection_search_radius, 
            y2=self.__cursor_y + self.__class__.selection_search_radius
        )
                
        focused_element_volatile_id: int = None
        
        try:
            closest_element_volatile_id: int = self.__canvas.find_closest(x=self.__cursor_x, y=self.__cursor_y)[0]
            if closest_element_volatile_id in overlapping_element_volatile_ids:
                focused_element_volatile_id = closest_element_volatile_id
        except IndexError:
            pass

        focused_element_id: int = None

        if focused_element_volatile_id is not None:
            focused_element_id = self.__element_volatile_id_id_lookup_table[focused_element_volatile_id]

        if focused_element_id != self.__focused_element_id:

            self.event_dispatcher.schedule_event_for_dispatch(
                event=Event(
                    trigger='FocusChanged',
                    payload={
                        'from': self.__focused_element_id,
                        'to': focused_element_id
                    }
                )
            )

            self.__focused_element_id = focused_element_id    
    
    def __motion(self, tk_event: tk.Event) -> None:

        self.__cursor_x = tk_event.x
        self.__cursor_y = tk_event.y

    def __left_click(self, tk_event: tk.Event) -> None:

        self.event_dispatcher.schedule_event_for_dispatch(
            event=Event(
                trigger='CanvasLeftClick',
                payload={
                    'tk_event': tk_event,
                    'focused_element_id': self.__focused_element_id
                }
            )
        )

    def __right_click(self, tk_event: tk.Event) -> None:

        self.event_dispatcher.schedule_event_for_dispatch(
            event=Event(
                trigger='CanvasRightClick',
                payload={
                    'tk_event': tk_event,
                    'focused_element_id': self.__focused_element_id
                }
            )
        )


if __name__ == '__main__':

    root = tk.Tk()

    engine = InteractiveCanvas(master=root)
    engine.frame.pack(expand=True, fill=tk.BOTH)

    class Point(InteractiveCanvas.CanvasElement):

        def __init__(self, x, y) -> None:
            super().__init__()

            self.x = x
            self.y = y

        def draw(self, context: tk.Canvas) -> int:
            return context.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5)

    from architecture.event.EventListener import EventListener
    from architecture.event.EventBus import EventBus
    from architecture.event.EventListener import EventNotRegisteredError

    points = []

    def make_point() -> None:
        point = Point(x=engine.cursor_position[0], y=engine.cursor_position[1])
        points.append(point)
        engine.new_element(element=point)
        engine.schedule_element_update(element_id=point.id)

    def make_it_rain() -> None:
        for point in points:
            point.y += 0.5
            engine.schedule_element_update(element_id=point.id)

    listener = EventListener()
    listener.register_event_handler(trigger='CanvasLeftClick', handler=make_point)
    listener.register_event_handler(trigger='UpdateEvent', handler=make_it_rain)
    listener.register_exception_handler(exception=EventNotRegisteredError, handler=lambda event: print(event))

    bus = EventBus()
    bus.add_listener(listener)
    engine.event_dispatcher.register_bus(bus)

    engine.issue_update_events()


    root.mainloop()