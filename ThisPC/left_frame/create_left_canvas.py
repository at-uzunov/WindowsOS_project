from tkinter import Canvas
from tkinter import Scrollbar

from ThisPC.left_frame.left_frame_content import LeftContent

class LeftCanvas(Canvas):

    def __init__(self, parent, frame_width, frame_height):
        super().__init__(parent)
        self.parent = parent
        self.height = frame_height
        self.width_scale = frame_width
        self.create_frame()

    def create_frame(self):
        self.left_canvas = Canvas(self.parent, height=self.height, width=self.width_scale, bg='white')
        self.left_canvas.grid(row=1, column=0, sticky='nwes')

        content = LeftContent(self.left_canvas, self.width_scale)
        content.run()

