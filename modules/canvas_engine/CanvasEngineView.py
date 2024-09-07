
from architecture.View import View
from architecture.event.Event import Event

import tkinter as tk
from abc import abstractmethod


class CanvasElement:

    def __init__(self, context: tk.Canvas) -> None:

        self._context: tk.Canvas = context 
        self._tag: int = None

    def delete(self) -> None:
        if self._tag is not None:
            self._context.delete(self._tag)
            self._tag = None

    @abstractmethod
    def draw(self) -> None:
        pass


class Point(CanvasElement):

    radius: int = 3
    fill: str = 'black'

    def __init__(self, context: tk.Canvas, x: int, y: int) -> None:
        CanvasElement.__init__(self, context=context)

        self.x: int = x
        self.y: int = y

    def draw(self) -> None:
        
        tag: str = self._context.create_oval(
            self.x + self.__class__.radius,
            self.y + self.__class__.radius,
            self.x - self.__class__.radius,
            self.y - self.__class__.radius,
            fill=self.__class__.fill
        )

        self._tag = tag


class Line(CanvasElement):

    width: int = 1

    def __init__(self, context: tk.Canvas, p0: Point, p1: Point) -> None:
        CanvasElement.__init__(self, context=context)

        self.p0: Point = p0
        self.p1: Point = p1
    
    def draw(self) -> None:

        tag: str = self._context.create_line(
            self.p0.x, 
            self.p0.y, 
            self.p1.x, 
            self.p1.y,
            width=self.__class__.width
        )

        self._tag = tag


class CanvasEngineView(View):

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

        self.__cursor_x: int = None
        self.__cursor_y: int = None

        self.__elements_scheduled_for_update: list[CanvasElement] = []

        self.__dynamic_elements: list[CanvasElement] = []
        self.__static_elements: list[CanvasElement] = []


        self.Binding(context=self.__canvas, identifier='CanvasMotion', sequence='<Motion>', func=self.__motion)
        self.Binding(context=self.__canvas, identifier='CanvasLeftClick', sequence='<Button-1>', func=self.__left_click)
        self.Binding(context=self.__canvas, identifier='CanvasRightClick', sequence='<Button-3>', func=self.__right_click)


        self.__element_creation_context: type = None

    def __run(self) -> None:
        self.__running = True
        self.frame.winfo_toplevel().after(self.__update_delay, self.__update)
        
    def __stop(self) -> None:
        self.__running = False

    def __update(self) -> None:
        self.__update_canvas_element_positions()
        self.__update_canvas()
        if self.__running:
            self.frame.winfo_toplevel().after(self.__update_delay, self.__update)

    def __update_canvas_element_positions(self) -> None:

        for element in self.__dynamic_elements:

            if isinstance(element, Point):

                element.x = self.__cursor_x
                element.y = self.__cursor_y

            elif isinstance(element, Line):
                
                element.p1.x = self.__cursor_x
                element.p1.y = self.__cursor_y

    def __update_canvas(self) -> None:

        for element in self.__elements_scheduled_for_update:
            element.delete()
            element.draw()

    def _enter(self, tk_event: tk.Event) -> None:

        self.bindings['CanvasMotion'].activate()
        self.bindings['CanvasLeftClick'].activate()
        self.bindings['CanvasRightClick'].activate()

        self.__run()

    def _leave(self, tk_event: tk.Event) -> None:

        self.bindings['CanvasMotion'].deactivate()
        self.bindings['CanvasLeftClick'].deactivate()
        self.bindings['CanvasRightClick'].deactivate()

        self.__stop()

    def set_element_creation_context(self, context: type) -> None:

        if context not in [Point, Line]:
            raise ValueError

        self.__element_creation_context = context


    def __motion(self, tk_event: tk.Event) -> None:

        self.__cursor_x = tk_event.x
        self.__cursor_y = tk_event.y


    def __left_click(self, tk_event: tk.Event) -> None:

        self.event_dispatcher.dispatch_event(
            event=Event(
                trigger='ElementCreation', 
                payload={
                    'tk_event': tk_event
                }
            )
        )



            

    def __right_click(self, tk_event: tk.Event) -> None:
        print(tk_event)


if __name__ == '__main__':

    root = tk.Tk()

    engine = CanvasEngineView(master=root)
    engine.frame.pack(expand=True, fill=tk.BOTH)
    engine.set_element_creation_context(context=Line)

    print(engine.view_type)

    root.mainloop()