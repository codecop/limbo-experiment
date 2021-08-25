# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X alle n Ticks kommt ein Glied dazu - von aussen gesteuert
- X auf User Input kann es rechts/links drehen - von aussen gesteuert
- X trifft Snake sich selbst ist Spiel aus - von aussen gesteuert
- X trifft Snake eine Wand ist Spiel aus - von aussen gesteuert
"""
from test_snake import Point
from test_game import Game, TurnCommand
from tkinter import Tk
from test_tk_view import TkView

import pytest
from unittest.mock import MagicMock

# create game: create Arena, create Snake, get View
# right/left pressed
# tick = draw on view
# game ended!


class Presenter:
    def __init__(self, view, game):
        self._view = view
        self._game = game
        self._next_command = None

        view.register_start_command(self.start)
        view.register_left_command(self.left)
        view.register_right_command(self.right)

    def left(self):
        self._next_command = TurnCommand.LEFT

    def right(self):
        self._next_command = TurnCommand.RIGHT

    def _loop(self):
        self._game.tick(self._next_command)
        self._next_command = None

        self._view.draw_snake(self._game.snake())
        self._view.draw_arena(self._game.arena())
        # TODO game over handling

    def start(self):
        # register _loop in schedule
        pass


@pytest.fixture
def viewGamePresenter():
    view = MagicMock()
    game = MagicMock()
    return view, game, Presenter(view, game)


def test_presenter_is_created_registers_keys(viewGamePresenter):
    view, _, _ = viewGamePresenter
    view.register_left_command.assert_called()
    view.register_right_command.assert_called()
    # view.register_start_command.assert_called()


def test_presenter_sets_command_right_only_once(viewGamePresenter):
    _, game, presenter = viewGamePresenter
    presenter.right()
    presenter._loop()
    game.tick.assert_called_with(TurnCommand.RIGHT)
    presenter._loop()
    game.tick.assert_called_with(None)


# turn left is just working ;-)


def test_presenter_draws_stuff(viewGamePresenter):
    view, game, presenter = viewGamePresenter
    game.snake = lambda: [Point(2, 3)]
    game.arena = lambda: [Point(8, 9)]
    presenter._loop()
    view.draw_snake.assert_called_with([Point(2, 3)])
    view.draw_arena.assert_called_with([Point(8, 9)])


def test_presenter_start_schedules_loop(viewGamePresenter):
    view, _, presenter = viewGamePresenter
    presenter.start()
    view.draw_snake.assert_called_with([Point(2, 3)])


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    game = Presenter(view)
    game.start()
    root.mainloop()
