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
    def __init__(self, root, width=100, height=100):
        self.window = root
        self.window.title("Snake")
        self._width = width
        self._height = height
        canvas = Canvas(
            root, width=self._width, height=self._height, background="white"
        )
        canvas.pack()
        self.canvas = canvas

        self._snake_objects = {}
        self._arena_objects = {}

    def draw_generic(self, new_points, point_object_mapping, fill, tags):

        old_points = point_object_mapping.keys()

        points_to_add = set(new_points) - set(old_points)
        points_to_remove = set(old_points) - set(new_points)

        # draw new points
        for point in points_to_add:
            point_object_mapping[point] = self.draw_point(point, fill=fill, tags=tags)

        # remove extra points
        for point in points_to_remove:
            self.canvas.delete(point_object_mapping.pop(point))

    def draw_snake(self, new_points):
        self.draw_generic(new_points, self._snake_objects, "green", ("snake"))

    def draw_arena(self, new_points):
        self.draw_generic(new_points, self._arena_objects, "grey", ("arena"))

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
        self.window.bind("<Return>", lambda event: callback())

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

        item_coords = [view.canvas.coords(item) for item in items]
        assert [45, 45, 55, 55] in item_coords
        assert [
            45 + 2 * RADIUS,
            45 - 4 * RADIUS,
            55 + 2 * RADIUS,
            55 - 4 * RADIUS,
        ] in item_coords

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

    def test_draw_new_snake_removes_old_snake(self):
        view = TkView(self.root)
        view.draw_snake([Point(0, 0)])
        view.draw_snake([Point(1, 0)])
        items = view.canvas.find_withtag("snake")
        assert 1 == len(items)


# right and start works ;-)
# arena works ;-)

if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    root.mainloop()
