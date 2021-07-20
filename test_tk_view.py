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
        for point in points:
            self.newmethod1(point)

    def newmethod1(self, point):
        xcenter = self._width / 2 + point.x * 2 * RADIUS
        ycenter = self._height / 2 - point.y * 2 * RADIUS
        x0 = xcenter - RADIUS
        x1 = xcenter + RADIUS
        y0 = ycenter - RADIUS
        y1 = ycenter + RADIUS
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="green", tags=("snake"))


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

    def test_view_draws_snake(self):
        view = TkView(self.root)
        view.draw_snake([Point(1, 2)])
        items = view.canvas.find_withtag("snake")
        assert 1 == len(items)

        item = items[0]
        assert [
            45 + 2 * RADIUS,
            45 - 4 * RADIUS,
            55 + 2 * RADIUS,
            55 - 4 * RADIUS,
        ] == view.canvas.coords(item)


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    root.mainloop()
