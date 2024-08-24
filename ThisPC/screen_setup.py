from tkinter import *

from ThisPC import first_page

class MainScreen(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.root = parent
        self.create_root()
        self.start()

    def create_root(self):
        self.screen_width = int(self.winfo_screenwidth() * 0.51)
        self.screen_height = int(self.winfo_screenheight() * 0.51)

        self.geometry(f'{self.screen_width}x{self.screen_height}+{int(self.screen_width*0.2)}+{int(self.screen_height*0.3)}')

    def start(self):
        self.wm_transient(self.root)
        first_page.run(self)
        self.root.mainloop()

