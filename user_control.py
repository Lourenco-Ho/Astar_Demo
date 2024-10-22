#import labrary
import show_gui
import numpy as np

#import my labrary
import a_star
import new_a_star
keycode = {
    "orig" : 49, #keyboard 1
    "dest" : 50 #keyboard 2
}

def key_press(event, frame_class):
    if event.keycode == keycode["orig"]:
        frame_class.orig_key_ispressed = True
    elif event.keycode == keycode["dest"]:
        frame_class.dest_key_ispressed = True


def key_release(event, frame_class):
    if event.keycode == keycode["orig"]:
        frame_class.orig_key_ispressed = False
    elif event.keycode == keycode["dest"]:
        frame_class.dest_key_ispressed = False


def on_board_unit_clicked(frame_class, coor):
    #clear path on screen
    for row_index, row_data in enumerate(frame_class.board_path):
        for column_index, column_data in enumerate(frame_class.board_path[row_index]):
            if column_data == 1:
                frame_class.board_path[row_index][column_index] = 0
                show_gui.show_normal(frame_class, {"x": column_index, "y": row_index})


    if frame_class.orig_key_ispressed:
        if frame_class.start != None:
            show_gui.show_normal(frame_class, {"x": frame_class.start[0], "y": frame_class.start[1]})
        frame_class.start = (coor["x"], coor["y"])
        show_gui.show_origin(frame_class, coor)
    elif frame_class.dest_key_ispressed:
        if frame_class.dest != None:
            show_gui.show_normal(frame_class, {"x": frame_class.dest[0], "y": frame_class.dest[1]})
        frame_class.dest = (coor["x"], coor["y"])
        show_gui.show_dest(frame_class, coor)
    else:
        if (frame_class.board[coor["y"]][coor["x"]] == 0):
            show_gui.show_block(frame_class, coor)
            frame_class.board[coor["y"]][coor["x"]] = 1
        else:
            show_gui.show_normal(frame_class, coor)
            frame_class.board[coor["y"]][coor["x"]] = 0

    #print(np.matrix(frame_class.board))
    #graph = a_star.spawn_graph(frame_class)
    #path = a_star.find_path(frame_class, graph, frame_class.start, frame_class.dest)
    path = new_a_star.a_star(frame_class.start, frame_class.dest, frame_class.board)

    #display the path
    if path != None:
        for index, point in enumerate(path):
            if index != 0 and index != len(path) -1:
                frame_class.board_path[point[1]][point[0]] = 1
                show_gui.show_route(frame_class, {"x": point[0], "y" : point[1]}, str(index))


def setup(window_class, frame_class):
    frame_class.orig_key_ispressed = False
    frame_class.dest_key_ispressed = False

    window_class.bind_all("<KeyPress>", lambda event: key_press(event, frame_class))
    window_class.bind_all("<KeyRelease>", lambda event: key_release(event, frame_class))