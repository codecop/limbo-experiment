# -*- coding: latin-1 -*-
"""
Snippet to demonstrate key event binding.
"""
import tkinter


KEYBOARD_EVENTS = [
    "Key",
    "Control-Up",
    "Return",
    "Escape",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F10",
    "F11",
    "F12",
    "Num_Lock",
    "Scroll_Lock",
    "Caps_Lock",
    "Print",
    "Insert",
    "Delete",
    "Pause",
    "Prior",
    "Next",
    "BackSpace",
    "Tab",
    "Cancel",
    "Control_L",
    "Alt_L",
    "Shift_L",
    "End",
    "Home",
    "Up",
    "Down",
    "Left",
    "Right",
]


def handle_key_event(event):
    print(
        "Event attributes: char={!r}, keysym={!r}, keycode={!r}".format(
            event.char, event.keysym, event.keycode
        )
    )


if __name__ == "__main__":

    root = tkinter.Tk()

    for keyboard_event in KEYBOARD_EVENTS:
        root.bind("<{}>".format(keyboard_event), handle_key_event)

    root.mainloop()
