from tkinter import *

from ThisPC.left_frame.create_left_canvas import LeftCanvas
from ThisPC.middle_frame.create_middle_canvas import MiddleCanvas
from ThisPC.top_frame.create_top_canvas import TopCanvas


def root_setup(parent):
    parent.grid_rowconfigure(1, weight=1)
    parent.grid_columnconfigure(1, weight=1)


def top_frame(parent, screen_width, screen_height):
    top_canvas = TopCanvas(parent, screen_width, screen_height)
    top_canvas.run()


def left_frame(parent, screen_width, screen_height):
    width = int(screen_width * 0.2)
    left_canvas = LeftCanvas(parent, width, screen_height)


def middle_frame(parent, screen_width, screen_height):
    middle_canvas = MiddleCanvas(parent, screen_width, screen_height)


def run(parent):
    screen_width = parent.screen_width
    screen_height = parent.screen_height

    root_setup(parent)
    left_frame(parent, screen_width, screen_height)
    top_frame(parent, screen_width, screen_height)
    middle_frame(parent, screen_width, screen_height)
