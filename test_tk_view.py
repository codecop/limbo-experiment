# -*- coding: latin-1 -*-
"""
TKinter implementation of domain view of game.
* draw snake
* draw arena
  * draw wall
* update/redraw
* ? key commands - könnte auch was anderes sein
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
RADIUS = 5


class TkView:
    def __init__(self, root):
        self.window = root
        self.window.title("Snake")
        self._width = 100
        self._height = 100
        canvas = Canvas(
            root, width=self._width, height=self._height, background="white"
        )
        canvas.pack()
        self.canvas = canvas

    def draw_snake(self, points):
        point = points[0]
        x0 = self._width / 2 - RADIUS
        x1 = self._width / 2 + RADIUS
        y0 = self._height / 2 - RADIUS
        y1 = self._height / 2 + RADIUS
        self.canvas.create_rectangle(45, 45, 55, 55, fill="green", tags=("snake"))


class TestTkView(TkinterTestCase):
    def test_window_title_is_snake(self):
        view = TkView(self.root)
        assert view.window.title() == "Snake"

    def test_view_draws_snake(self):
        view = TkView(self.root)
        view.draw_snake([Point(0, 0)])
        items = view.canvas.find_withtag("snake")
        assert 1 == len(items)

        item = items[0]
        assert [45, 45, 55, 55] == view.canvas.coords(item)


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    root.mainloop()
