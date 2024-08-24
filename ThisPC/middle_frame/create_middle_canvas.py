from tkinter import Canvas

from ThisPC.middle_frame.middle_frame_content import Drives


class MiddleCanvas(Canvas):
    def __init__(self, parent, screen_width, screen_height):
        super().__init__(parent)
        self.parent = parent
        self.width = int(screen_width * 0.8)
        self.height = screen_height
        self.create_frame()

    def create_frame(self):
        middle_canvas = Canvas(self.parent, height=self.height, width=self.width, bg='white')
        middle_canvas.grid(row=1, column=1, sticky='nsew')

        test = Drives(middle_canvas)
