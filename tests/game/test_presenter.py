# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X alle n Ticks kommt ein Glied dazu - von aussen gesteuert
- X auf User Input kann es rechts/links drehen - von aussen gesteuert
- X trifft Snake sich selbst ist Spiel aus - von aussen gesteuert
- X trifft Snake eine Wand ist Spiel aus - von aussen gesteuert
"""
from unittest.mock import MagicMock

import pytest

from game.game import TurnCommand
from game.presenter import Presenter
from game.snake import Point


@pytest.fixture
def viewGamePresenter():
    view = MagicMock()
    game = MagicMock()
    return view, game, Presenter(view, game)


def test_presenter_is_created_registers_keys(viewGamePresenter):
    view, _, _ = viewGamePresenter
    view.register_left_command.assert_called()
    view.register_right_command.assert_called()
    view.register_start_command.assert_called()


def test_presenter_sets_command_right_only_once(viewGamePresenter):
    _, game, presenter = viewGamePresenter
    presenter.right()
    presenter._loop()
    game.tick.assert_called_with(TurnCommand.RIGHT)
    presenter._loop()
    game.tick.assert_called_with(None)


# turn left is just working ;-)


def test_presenter_draws_stuff_in_loop(viewGamePresenter):
    # is related to test_game.test_new_game_has_snake
    # make sure they match
    # TBD: custom assertions to simplify tests with real game/arena/snake?
    view, game, presenter = viewGamePresenter
    game.snake = lambda: [Point(2, 3)]
    game.arena = lambda: [Point(8, 9)]
    presenter._loop()
    view.draw_snake.assert_called_with([Point(2, 3)])
    view.draw_arena.assert_called_with([Point(8, 9)])


def test_presenter_reschedules_loop(viewGamePresenter):
    view, _, presenter = viewGamePresenter
    presenter._loop()
    view.schedule_tick.assert_called()


def test_presenter_start_schedules_loop_and_draws_stuff(viewGamePresenter):
    view, _, presenter = viewGamePresenter
    presenter.start()
    view.schedule_tick.assert_called()
    view.draw_snake.assert_called()
    view.draw_arena.assert_called()


# game over handling


def test_presenter_does_not_reschedules_loop_on_game_over(viewGamePresenter):
    view, game, presenter = viewGamePresenter
    game.is_running = lambda: False
    presenter._loop()
    view.schedule_tick.assert_not_called()


def test_presenter_notifies_view_on_game_over(viewGamePresenter):
    view, game, presenter = viewGamePresenter
    game.is_running = lambda: False
    presenter._loop()
    view.game_over.assert_called()
