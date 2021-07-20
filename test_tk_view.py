# -*- coding: latin-1 -*-
"""
TKinter implementation of domain view of game.
* draw snake
* draw arena
  * draw wall
* update/redraw
* ? key commands - k�nnte auch was anderes sein
* extras
  * game over state
  * display score
  * start new game
  * Tick speed
* "Game Loop" = tick wird scheduled
"""
from test_snake import Point

from tkinter import Tk, Canvas
from tkinter_snippets.test_util import TkinterTestCase

import pytest

# registerGameTick, time
# register cursorr keys callback

# print_snake(points)
# print_arena(points)

# registerViewModel(model)
# update


class TkView:
    def __init__(self, root):
        self.window = root
        self.window.title("Snake")
        canvas = Canvas(root, width=100, height=100, background="white")
        canvas.pack()
        self.canvas = canvas

    def draw_snake(self, points):
        pass


class TestTkView(TkinterTestCase):
    def test_window_title_is_snake(self):
        view = TkView(self.root)
        assert view.window.title() == "Snake"

    def test_view_draws_snake(self):
        view = TkView(self.root)
        view.draw_snake([(0, 0)])
        items = view.canvas.find_withtag("snake")
        # assert 1 == len(items)
        # assertThatUiHasBluePixelAt(100,100)


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    root.mainloop()
