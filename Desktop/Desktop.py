from tkinter import *
from Desktop.DesktopUI import DesktopUi

class Desktop:

    def __init__(self):
        self.root = Tk()
        self.root_setup()
        self.desktop_canvas()
        self.ui_creating()

    def ui_creating(self):
        ui = DesktopUi(self)

    def root_setup(self):
        self.screen_width = int(self.root.winfo_screenwidth() * 0.834)
        self.screen_height = int(self.root.winfo_screenheight() * 0.83)

        self.root.geometry(
            f'{self.screen_width}x{self.screen_height}+{int(self.screen_width * 0.1)}+{int(self.screen_height * 0.05)}')

    def desktop_canvas(self):
        main_background = PhotoImage(file="Desktop/Images/background.png")

        self.main_canvas = Canvas(self.root, width=self.screen_width, height=int(self.screen_height))
        self.main_canvas.grid_propagate(False)
        for i in range(14):
            self.main_canvas.grid_rowconfigure(i, minsize=64)

        for i in range(25):
            self.main_canvas.grid_columnconfigure(i, minsize=64)

        self.main_canvas.create_image(0, 0, image=main_background, anchor='nw')
        self.main_canvas.image = main_background
        self.main_canvas.grid(row=0, column=0, sticky='nsew', columnspan=25, rowspan=14)

    def run(self):
        self.root.mainloop()
