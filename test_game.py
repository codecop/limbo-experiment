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

# create game: create Arena, create Snake, get View
# right/left pressed
# tick = draw on view
# grow


class Game:
    def __init__(self, view):
        self._view = view

    def start(self):
        pass


class MockView:
    pass


def test_foo():
    view = 1
    game = Game(view)


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    game = Game(view)
    game.start()
    root.mainloop()
