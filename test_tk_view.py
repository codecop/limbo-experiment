# -*- coding: latin-1 -*-
"""
TKinter implementation of domain view of game.
* X draw snake
* X draw arena
  * X draw wall
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

# Skipped
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

        self._snake_objects = {}

    def draw_snake(self, points):
        for point in points:
            if point in self._snake_objects:
                continue
            self._snake_objects[point] = self.draw_point(
                point, fill="green", tags=("snake")
            )

    def draw_arena(self, points):
        for point in points:
            self.draw_point(point, fill="grey", tags=("arena"))

    # TODO: remove old drawings
    def draw_point(self, point, fill, tags):
        xcenter = self._width / 2 + point.x * 2 * RADIUS
        ycenter = self._height / 2 - point.y * 2 * RADIUS
        x0 = xcenter - RADIUS
        x1 = xcenter + RADIUS
        y0 = ycenter - RADIUS
        y1 = ycenter + RADIUS
        return self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, tags=tags)

    def register_left_command(self, callback):
        self.left_command = callback
        self.window.bind("<Left>", lambda event: callback())

    def register_right_command(self, callback):
        self.left_command = callback
        self.window.bind("<Right>", lambda event: callback())

    def register_start_command(self, callback):
        self.start_command = callback
        self.window.bind("<Enter>", lambda event: callback())

    def schedule_tick(self, callback, millis):
        # not TDD/TCR because cannot test TKinter scheduling
        self.window.after(millis, callback)


class TestTkView(TkinterTestCase):
    def test_window_title_is_snake(self):
        view = TkView(self.root)
        assert view.window.title() == "Snake"

    def test_view_draws_snake(self):
        view = TkView(self.root)
        view.draw_snake([Point(0, 0), Point(1, 2)])
        items = view.canvas.find_withtag("snake")
        assert 2 == len(items)

        item = items[0]
        assert [45, 45, 55, 55] == view.canvas.coords(item)

        item = items[1]
        assert [
            45 + 2 * RADIUS,
            45 - 4 * RADIUS,
            55 + 2 * RADIUS,
            55 - 4 * RADIUS,
        ] == view.canvas.coords(item)

    def test_command_key_left(self):
        view = TkView(self.root)

        self._was_callback_called = False

        def callback():
            self._was_callback_called = True

        view.register_left_command(callback)
        view.window.event_generate("<Left>")

        assert self._was_callback_called is True

    # do not draw what is there

    def test_draw_same_snake_twice_draws_only_once(self):
        view = TkView(self.root)
        view.draw_snake([Point(0, 0), Point(1, 2)])
        view.draw_snake([Point(0, 0), Point(1, 2)])
        items = view.canvas.find_withtag("snake")
        assert 2 == len(items)


# right and start works ;-)

if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    root.mainloop()
