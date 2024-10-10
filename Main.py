#import labrary
from tkinter import *

import show_gui
import board_appearance
import user_control


class a_star_demo(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        self.title(board_appearance.app_name)

        self.attributes("-fullscreen", True)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frame = globals()["ui_frame"]
        frame = frame(window_frame=container, window_class=self)
        frame.config(**board_appearance.app_window_config)
        frame.grid(row=0, column=0, sticky = "nsew")
        frame.tkraise()


class ui_frame(Frame):
    def __init__(frame_class, window_frame, window_class):
        Frame.__init__(frame_class, window_frame)

        #spawn layout
        frame_class.board = [[0 for column in range(board_appearance.board_size["width"]) ] for row in range(board_appearance.board_size["height"])]
        frame_class.board_path = [[0 for column in range(board_appearance.board_size["width"]) ] for row in range(board_appearance.board_size["height"])]

        frame_class.start = None
        frame_class.dest = None
        show_gui.spawn_layout(frame_class)
        user_control.setup(window_class, frame_class)


if __name__ == "__main__":
    a_star_demo().mainloop()