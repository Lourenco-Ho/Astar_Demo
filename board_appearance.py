#app main
app_name = "A* Algorithm Demo"
app_window_config = {
    "highlightbackground" : "black",
    "highlightthickness" : 1
}


#board
board_size = {
    "height" : 10,
    "width" : 10
}

unit_size = 50

square_btn_config = {
    "text" : "",
    "font" : ('Arial', 45, 'bold'),
    "highlightbackground" : "black",
    "highlightthickness" : 2,
    "bg" : "gray80",
}

normal_config = {
    "text" : "",
    "font" : ('Arial', 45, 'bold'),
    "fg" : "black",
    "bg" : "gray80",
}


origin_config = {
    "text" : "O",
    "font" : ('Arial', 45, 'bold'),
    "fg" : "green",
    "bg" : "gray80",
}

dest_config = {
    "text" : "O",
    "font" : ('Arial', 45, 'bold'),
    "fg" : "red",
    "bg" : "gray80",
}


def route_config(text):
    config = {
        "text" : text,
        "font" : ('Arial', 45, 'bold'),
        "fg" : "black",
        "bg" : "red",
    }
    return config

def run_config(text):
    config = {
        "text" : text,
        "font" : ('Arial', 12, 'bold'),
        "fg" : "black",
        "bg" : "blue",
    }
    return config

block_config = {
    "text" : "",
    "font" : ('Arial', 45, 'bold'),
    "fg" : "black",
    "bg" : "black",
}
