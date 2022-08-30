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
from game.square_geometry import Point


@pytest.fixture
def view_game_presenter():
    view = MagicMock()
    game = MagicMock()
    return view, game, Presenter(view, game)


def test_presenter_is_created_registers_keys(view_game_presenter):
    view, _, _ = view_game_presenter
    view.register_left_command.assert_called()
    view.register_right_command.assert_called()
    view.register_start_command.assert_called()


def test_presenter_sets_command_right_only_once(view_game_presenter):
    _, game, presenter = view_game_presenter
    presenter.right()
    presenter._loop()
    game.tick.assert_called_with(TurnCommand.RIGHT)
    presenter._loop()
    game.tick.assert_called_with(None)


# turn left is just working ;-)


def test_presenter_draws_stuff_in_loop(view_game_presenter):
    # is related to test_game.test_new_game_has_snake
    # make sure they match
    # TBD: custom assertions to simplify tests with real game/arena/snake?
    view, game, presenter = view_game_presenter
    game.snake = lambda: [Point(2, 3)]
    game.arena = lambda: [Point(8, 9)]
    game.apples = lambda: [Point(4, 6)]
    presenter._loop()
    view.draw_snake.assert_called_with([Point(2, 3)])
    view.draw_arena.assert_called_with([Point(8, 9)])
    view.draw_apples.assert_called_with([Point(4, 6)])


def test_presenter_reschedules_loop(view_game_presenter):
    view, _, presenter = view_game_presenter
    presenter._loop()
    view.schedule_tick.assert_called()


def test_presenter_start_schedules_loop_and_draws_stuff(view_game_presenter):
    view, _, presenter = view_game_presenter
    presenter.start()
    view.schedule_tick.assert_called()
    view.draw_snake.assert_called()
    view.draw_arena.assert_called()


# game over handling

# TODO fix typing
# TODO little bit of duplication here
def test_presenter_does_not_reschedules_loop_on_game_over(view_game_presenter):
    view, game, presenter = view_game_presenter
    game.is_running = lambda: False
    presenter._loop()
    view.schedule_tick.assert_not_called()


def test_presenter_notifies_view_on_game_over(view_game_presenter):
    view, game, presenter = view_game_presenter
    game.is_running = lambda: False
    presenter._loop()
    view.game_over.assert_called()
