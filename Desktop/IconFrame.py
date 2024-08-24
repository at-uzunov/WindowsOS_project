from tkinter import *

import os
import threading

script_dir = os.path.dirname(os.path.abspath(__file__))


class IconFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, background='silver')
        self.parent = parent
        self.grid(row=0, column=0, sticky='nwse')
        self.count = 0
        self.create_icons()

    def create_icons(self):
        image_path = os.path.join(script_dir, 'desktop_icons')
        img = PhotoImage(file=image_path + '/pc.png')
        label = Label(self.parent, image=img,bg='orange')
        label.image = img
        label.bind("<Button-1>", self.open_thispc)
        label.grid(row=0, column=0)

    def open_thispc(self, e):
        self.count += 1
        #if self.count == 1:
            #first_page.run()
        #else:
           # self.count = 0
            #first_page.root.destroy()


