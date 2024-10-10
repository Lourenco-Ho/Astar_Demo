from tkinter import *
import board_appearance
import user_control

def spawn_layout(frame_class):
    frame_class.Frame = Frame(frame_class)
    frame_class.grid_rowconfigure(0, weight=1)
    frame_class.grid_columnconfigure(0, weight=1)

    frame_class.Frame.grid(row=0, column=0)

    frame_class.board_label = [[board_unit(frame_class, {"x": column, "y": row}) for column in range(board_appearance.board_size["width"])]for row in range(board_appearance.board_size["height"])]


def board_unit(frame_class, coor):
    label_frame = Frame(frame_class.Frame, width=board_appearance.unit_size, height=board_appearance.unit_size)
    label_frame.grid_propagate(False) #disables resizing of frame
    label_frame.columnconfigure(0, weight=1) #enables label to fill frame
    label_frame.rowconfigure(0,weight=1) #any positive number would do the trick
    label_frame.grid(row=coor["y"], column=coor["x"])

    square_button = Button(label_frame,command=lambda: user_control.on_board_unit_clicked(frame_class, coor), **board_appearance.square_btn_config)
    square_button.grid(sticky="wens")

    return square_button


def show_normal(frame_class, coor):
    frame_class.board_label[ coor["y"] ] [ coor["x"] ].config(**board_appearance.normal_config)

def show_block(frame_class, coor):
    frame_class.board_label[ coor["y"] ] [ coor["x"] ].config(**board_appearance.block_config)


def show_origin(frame_class, coor):
    frame_class.board_label[ coor["y"] ] [ coor["x"] ].config(**board_appearance.origin_config)


def show_dest(frame_class, coor):
    frame_class.board_label[ coor["y"] ] [ coor["x"] ].config(**board_appearance.dest_config)

def show_route(frame_class, coor, text):
    frame_class.board_label[ coor["y"] ] [ coor["x"] ].config(**board_appearance.route_config(text))