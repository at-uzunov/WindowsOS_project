from tkinter import Canvas

from ThisPC.top_frame.top_frame_content import Cont


class TopCanvas:
    def __init__(self, parent, frame_width, frame_height):
        self.parent = parent
        self.width = frame_width
        self.height = int(frame_height * 0.28)

    def create_cavnas(self):
        self.top_canvas = Canvas(self.parent, width=self.width, height=self.height, bg='white')
        self.top_canvas.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.top_canvas.grid_propagate(False)
        return self.top_canvas

    def run_content(self):
        cont = Cont(self.top_canvas, self.parent, self.width)
        cont.run()

    def run(self):
        self.create_cavnas()
        self.run_content()
