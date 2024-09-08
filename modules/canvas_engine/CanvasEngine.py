
from architecture.View import View
from architecture.event.Event import Event

import tkinter as tk
from abc import abstractmethod
from typing import Hashable

t_CanvasId = int
t_ElementId = int


class CanvasElement:

    __canvas_element_counter: int = 0

    def __init__(self, context: tk.Canvas) -> None:

        self.__id: int = self.__class__.__canvas_element_counter
        self.__class__.__canvas_element_counter += 1

        self.__canvas_id: int = None

        self._context: tk.Canvas = context 
        self._tag: int = None

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def canvas_id(self) -> int:
        return self.__canvas_id

    def set_state(self, state: str) -> None:
        pass

    def delete(self) -> None:
        if self._tag is not None:
            self._context.delete(self._tag)
            self._tag = None

    def draw(self) -> None:
        pass

    def _draw(self) -> None:

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
            fill=self.__class__.fill,
            tags=('Selectable', 'Highlightable')
        )

        self.__canvas_id = tag


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



class CanvasEngine(View):

    selection_search_radius: int = 5

    def __init__(self, master: tk.Tk | tk.Toplevel | tk.Frame) -> None:
        View.__init__(self, master=master)

        # canvas styles

        self.__canvas: tk.Canvas = tk.Canvas(master=self.frame)
        self.__canvas.pack(expand=True, fill=tk.BOTH)

        self.__canvas.config(
            background='grey',
            cursor='crosshair'
        )

        # engine refresh

        self.__running: bool = False
        self.__update_delay: int = 33

        # engine data

        self.__cursor_x: int = None
        self.__cursor_y: int = None

        self.__new_canvas_elements: list[CanvasElement] = []
        self.__canvas_elements: dict[t_CanvasId, CanvasElement] = {}
        self.__canvas_element_ids_scheduled_for_update: list[t_CanvasId] = []

        self.__soft_selection_element_id: t_CanvasId = None
        self.__hard_selection_element_ids: list[t_CanvasId] = []

        # engine state

        self.__element_creation_context: type = None

        # bindings

        self.Binding(context=self.__canvas, identifier='CanvasMotion', sequence='<Motion>', func=self.__motion)
        self.Binding(context=self.__canvas, identifier='CanvasLeftClick', sequence='<Button-1>', func=self.__left_click)
        self.Binding(context=self.__canvas, identifier='CanvasRightClick', sequence='<Button-3>', func=self.__right_click)

        self._dynamic_binding_list = ['CanvasMotion', 'CanvasLeftClick', 'CanvasRightClick']


    def __run(self) -> None:

        self.__running = True
        self.frame.winfo_toplevel().after(self.__update_delay, self.__update)
        
    def __stop(self) -> None:
        self.__running = False

    def __update(self) -> None:

        self.__update_element_positions()
        self.__update_element_soft_selection_state()
        self.__update_element_hard_selection_state()
        self.__draw_elements_scheduled_for_update()
        self.__draw_new_elements()

        if self.__running:
            self.frame.winfo_toplevel().after(self.__update_delay, self.__update)

    def __update_element_positions(self) -> None:
        pass

    def __update_element_soft_selection_state(self) -> None:

        overlapping_element_ids: tuple[t_CanvasId] = self.__canvas.find_overlapping(
            x1=self.__cursor_x - self.__class__.selection_search_radius, 
            y1=self.__cursor_y - self.__class__.selection_search_radius, 
            x2=self.__cursor_x + self.__class__.selection_search_radius, 
            y2=self.__cursor_y + self.__class__.selection_search_radius
        )
                
        selection_element_id: t_CanvasId = None
        
        try:
            closest_element_id: t_CanvasId = self.__canvas.find_closest(x=self.__cursor_x, y=self.__cursor_y)[0]
            if closest_element_id in overlapping_element_ids:
                selection_element_id = closest_element_id
        except IndexError:
            pass

        print(self.__canvas_elements)
        
        if self.__soft_selection_element_id is None and selection_element_id is not None:

            self.__canvas_elements[selection_element_id].set_state(state='SoftSelect')
            self.__canvas_element_ids_scheduled_for_update.append(selection_element_id)
            self.__soft_selection_element_id = selection_element_id

        elif self.__soft_selection_element_id is not None and selection_element_id is not None:

            self.__canvas_elements[self.__soft_selection_element_id].set_state(state=None)
            self.__canvas_elements[selection_element_id].set_state(state='SoftSelect')
            self.__canvas_element_ids_scheduled_for_update.append(self.__soft_selection_element_id)
            self.__canvas_element_ids_scheduled_for_update.append(selection_element_id)
            self.__soft_selection_element_id = selection_element_id

        elif self.__soft_selection_element_id is not None and selection_element_id is None:

            self.__canvas_elements[self.__soft_selection_element_id].set_state(state=None)
            self.__canvas_element_ids_scheduled_for_update.append(self.__soft_selection_element_id)
            self.__soft_selection_element_id = None
            



    def __update_element_hard_selection_state(self) -> None:
        pass
 
    def __draw_new_elements(self) -> None:

        for element in self.__new_canvas_elements:

            element.draw()
            self.__canvas_elements[element.canvas_id] = element
        
        self.__new_canvas_elements = []

    def __draw_elements_scheduled_for_update(self) -> None:

        for element_id in self.__canvas_element_ids_scheduled_for_update:
            element: CanvasElement = self.__canvas_elements[element_id]

            previous_canvas_id: int = element.canvas_id
            
            element.delete()
            element.draw()

            current_canvas_id: int = element.canvas_id

            del self.__canvas_elements[previous_canvas_id]
            self.__canvas_elements[current_canvas_id] = element
            element.canvas_id = current_canvas_id

        self.__canvas_element_ids_scheduled_for_update = []


    def _enter(self, tk_event: tk.Event) -> None:
        self.__run()

    def _leave(self, tk_event: tk.Event) -> None:
        self.__stop()

    def set_element_creation_context(self, context: type) -> None:

        if context not in [Point, Line]:
            raise ValueError

        self.__element_creation_context = context

    def __motion(self, tk_event: tk.Event) -> None:

        self.__cursor_x = tk_event.x
        self.__cursor_y = tk_event.y

    def __left_click(self, tk_event: tk.Event) -> None:
        print(tk_event)

        if self.__element_creation_context == Point:

            point: Point = Point(context=self.__canvas, x=self.__cursor_x, y=self.__cursor_y)
            self.__new_canvas_elements.append(point)

    def __right_click(self, tk_event: tk.Event) -> None:
        print(tk_event)


if __name__ == '__main__':

    root = tk.Tk()

    engine = CanvasEngineView(master=root)
    engine.frame.pack(expand=True, fill=tk.BOTH)
    engine.set_element_creation_context(context=Point)

    print(engine.view_type)

    root.mainloop()