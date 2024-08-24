from tkinter import *
from Desktop.Start_Menu.Start_Menu_Frame_Content import Start_Menu_Frame_Content01


class Start_Menu_Frame(Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent.main_canvas, background='#F4F6F9', width=660, height=720)
        super().grid_propagate(False)
        self.grid(row=1, column=5, columnspan=14, rowspan=14)
        for i in range(14):
            self.columnconfigure(i, minsize=64)
        for i in range(15):
            self.rowconfigure(i, minsize=64)
        buttons = Start_Menu_Frame_Content01(self, self.parent)
