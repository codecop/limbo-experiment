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
from unittest.mock import MagicMock

# create game: create Arena, create Snake, get View
# right/left pressed
# tick = draw on view
# grow
# game ended!


class Presenter:
    def __init__(self, view):
        self._view = view
        view.register_left_command(self.left)
        view.register_right_command(self.right)

    def left(self):
        # set command LEFT
        pass

    def right(self):
        # set command RIGHT
        pass

    def _loop(self):
        # self._game_tick(command)
        # draw snake and draw arena
        pass

    def start(self):
        # register _lop in schedule
        pass


class MockView:
    def __init__(self):
        self.register_left_command_has_been_called = False
        self.register_right_command_has_been_called = False

    def draw_snake(self, points):
        pass

    def draw_arena(self, points):
        pass

    def register_left_command(self, callback):
        self.register_left_command_has_been_called = True

    def register_right_command(self, callback):
        self.register_right_command_has_been_called = True

    def schedule_tick(self, callback, millis):
        pass


def test_presenter_is_created_registers_keys():
    view = MockView()
    Presenter(view)
    assert view.register_left_command_has_been_called is True
    assert view.register_right_command_has_been_called is True


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    game = Presenter(view)
    game.start()
    root.mainloop()
