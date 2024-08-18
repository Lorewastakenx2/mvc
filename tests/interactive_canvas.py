
from widgets.InteractiveCanvas import InteractiveCanvas


import tkinter as tk

if __name__ == '__main__':

    root = tk.Tk()

    widget = InteractiveCanvas()
    widget.view.initialize(master=root)
    widget.view.frame.pack(expand=True, fill=tk.BOTH)


    root.mainloop()
