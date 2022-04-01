# -*- coding: latin-1 -*-
from tkinter import Tk

from conftest import (
    skipifcontainer_because_event_handling_not_working,
)  # TODO: resolve differently
from tkutil.testing import TkinterTestCase
from game.snake import Point
from game.tkview import RADIUS, TkView


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

    @skipifcontainer_because_event_handling_not_working
    def test_command_key_left_triggers_associated_callback(self):
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

    def test_game_over_draws_message(self):
        view = TkView(self.root)
        view.game_over()
        items = view.canvas.find_withtag("gameover")
        assert 1 == len(items)

    def test_game_start_draws_message(self):
        view = TkView(self.root)
        view.game_start()
        items = view.canvas.find_withtag("gamestart")
        assert 1 == len(items)

    def test_draw_apple(self):
        view = TkView(self.root)
        view.draw_snake([Point(0, 0), Point(1, 2)])
        items = view.canvas.find_withtag("snake")
        assert 2 == len(items)


# right and start works ;-)
# arena works ;-)

if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    root.mainloop()
