# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X alle n Ticks kommt ein Glied dazu - von aussen gesteuert
- X auf User Input kann es rechts/links drehen - von aussen gesteuert
- X trifft Snake sich selbst ist Spiel aus - von aussen gesteuert
- X trifft Snake eine Wand ist Spiel aus - von aussen gesteuert
"""
from test_game import Game
from tkinter import Tk
from test_tk_view import TkView

import pytest
from unittest.mock import MagicMock

# create game: create Arena, create Snake, get View
# right/left pressed
# tick = draw on view
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


@pytest.fixture
def view():
    return MagicMock()


@pytest.fixture
def game():
    return MagicMock()


def fixture():
    view = MagicMock()
    # game = Game()
    return view, Presenter(view)


def test_presenter_is_created_registers_keys():
    view = MagicMock()
    Presenter(view)
    view.register_left_command.assert_called()
    view.register_right_command.assert_called()


def test_presenter_sets_command_left():
    pass


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    game = Presenter(view)
    game.start()
    root.mainloop()
