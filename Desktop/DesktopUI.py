from tkinter import *
from Desktop.ButtonActions import ButtonActions


class DesktopUi:
    def __init__(self, parent):
        self.parent = parent
        self.button_actions = ButtonActions(self.parent)
        self.thispc_icon()
        self.collection_manager_icon()
        self.menu_bar()

    def thispc_icon(self):
        img = PhotoImage(file='ThisPC/left_frame/left_frame_icons/thispc/pc.png')
        label = Label(self.parent.main_canvas, image=img, text='This PC', bg='white', compound='top')
        label.image = img
        label.grid(row=0, column=0)

        label.bind('<Button-1>', self.button_actions.thispc_run)
        label.bind('<Enter>', self.on_enter)
        label.bind('<Leave>', self.on_leave)

    def collection_manager_icon(self):
        img = PhotoImage(file='CollectionManager/Icons/logo.png')
        label = Label(self.parent.main_canvas, image = img,
                      bg='white',
                      compound='top', wraplength=40)
        label.image=img
        label.grid(row=1, column=0)

        label.bind('<Button-1>', self.button_actions.collection_manager)
        label.bind('<Enter>', self.on_enter)
        label.bind('<Leave>', self.on_leave)

    def menu_bar(self):
        bar_frame = Frame(self.parent.main_canvas, background='#E1E9F9')
        bar_frame.grid(row=13, column=0, sticky="sew", columnspan=25)
        for i in range(25):
            bar_frame.columnconfigure(i, minsize=64)
        start_menu_icon = PhotoImage(file="Desktop/Images/start_menu.png")
        start_menu_icon = start_menu_icon.subsample(x=4, y=4)

        start_menu = Button(bar_frame, image=start_menu_icon, background='white',
                            command=self.button_actions.place_frame)
        start_menu.image = start_menu_icon
        start_menu.grid(row=0, column=8)

        label = Label(bar_frame, text='Test', background='white')
        label.grid(row=0, column=0, sticky='nsew')

    def run(self):
        self.menu_bar()

    def on_enter(self, e):
        e.widget.configure(bg='lightblue1')

    def on_leave(self, e):
        e.widget.configure(bg='white')
