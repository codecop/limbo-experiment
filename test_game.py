# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X alle n Ticks kommt ein Glied dazu - von aussen gesteuert
- X auf User Input kann es rechts/links drehen - von aussen gesteuert
- X trifft Snake sich selbst ist Spiel aus - von aussen gesteuert
- X trifft Snake eine Wand ist Spiel aus - von aussen gesteuert
"""
from tkinter import Tk
from test_snake import Point, Snake
from test_arena import Arena
from test_tk_view import TkView

import pytest


def test_foo():
    pass


if __name__ == "__main__":
    root = Tk()
    # view = TkView(root)
    # root.mainloop()
