# -*- coding: latin-1 -*-
from unittest.mock import Mock

import pytest
from game.arena import Arena

from game.game import Game, TurnCommand
from game.game import Cycle
from game.geometry import Box, Point
from game.snake import Snake


# TBD: Could these tests be simplified?
def test_new_game_has_snake(game):
    snake_coordinates = game.snake()
    assert snake_coordinates == [Point(0, 0), Point(0, -1), Point(0, -2)]


def test_new_game_has_arena(game):
    arena_coordinates = game.arena()
    assert len(arena_coordinates) == 4 + 7 + 7 + 5 + 5


# APPLE TESTS
#############
def test_new_game_has_initial_apple(game):
    apple_coordinates = game.apples()
    assert apple_coordinates == [Point(0, 1)]


def test_game_can_set_apples(big_game):
    assert len(big_game.apples()) == 1
    for _ in range(10):
        big_game.tick()
    assert len(big_game.apples()) == 2


def test_game_sets_apples_at_different_locations(big_game):
    for _ in range(10 + 10):  # 10 is ticks_to_apple in big_game
        big_game.tick()
    assert len(set(big_game.apples())) == 1 + 2


@pytest.mark.parametrize("execution_number", range(10))
def test_game_sets_apple_not_at_snake(execution_number):
    # random_point has 1/5 probability to not have coverage
    snake = Snake()
    snake.grow()
    arena = Arena(Box(1, 3))
    game = Game(snake, arena, grow_count=99, apple_count=1)

    game.tick()

    assert len(game.apples()) == 1
    assert game.apples()[0] == Point(0, 2)


# SNAKE TESTS
#############
def test_game_tick_moves_snake(game):
    game.tick()
    snake_coordinates = game.snake()
    assert snake_coordinates == [Point(0, 1), Point(0, 0), Point(0, -1)]


def test_game_tick_turn_left_rotates_and_moves_snake(game):
    game.tick(TurnCommand.LEFT)
    snake_coordinates = game.snake()
    assert snake_coordinates == [Point(-1, 0), Point(0, 0), Point(0, -1)]


def test_game_tick_turn_right_rotates_and_moves_snake(game):
    game.tick(TurnCommand.RIGHT)
    snake_coordinates = game.snake()
    assert snake_coordinates == [Point(1, 0), Point(0, 0), Point(0, -1)]


def test_new_game_is_running(game):
    assert game.is_running() is True


def test_game_is_over_if_snake_hits_the_wall(game):
    game.tick()
    game.tick()
    game.tick()
    assert game.is_running() is True
    game.tick()
    assert game.is_running() is False


def test_if_game_is_over_stop_advancing_snake(game):
    game.tick()
    game.tick()
    game.tick()
    game.tick()
    old_snake_coordinates = game.snake()
    game.tick()
    new_snake_coordinates = game.snake()
    assert old_snake_coordinates == new_snake_coordinates


def test_game_grows_snake_every_3_ticks(game):
    game.tick()
    game.tick()
    old_snake_length = len(game.snake())
    game.tick()
    new_snake_length = len(game.snake())
    assert new_snake_length == old_snake_length + 1


def test_if_snake_hits_itself_game_is_over(game):
    game.tick(TurnCommand.RIGHT)
    game.tick(TurnCommand.RIGHT)
    game.tick(TurnCommand.RIGHT)  # grow
    assert game.is_running() is True
    game.tick(TurnCommand.RIGHT)
    game.tick(TurnCommand.RIGHT)
    assert game.is_running() is True
    game.tick(TurnCommand.RIGHT)  # grow
    assert game.is_running() is False


def test_snake_grows_when_eating_an_apple(game):
    old_snake_length = len(game.snake())
    # snake starts at 0,0
    game.tick()  # ends at 0,1, eats apple but not grown yet
    game.tick()  # has grown
    new_snake_length = len(game.snake())
    assert new_snake_length == old_snake_length + 1


def test_apple_is_removed_when_eaten(game):
    old_snake_length = len(game.snake())
    game.tick()
    game.tick(TurnCommand.RIGHT)  # grown due to apple
    game.tick(TurnCommand.RIGHT)  # grow
    game.tick()
    game.tick()
    game.tick(TurnCommand.RIGHT)  # grow
    game.tick(TurnCommand.RIGHT)
    game.tick()
    game.tick()  # grow, and would eat apple again
    game.tick()  # has NOT grown
    new_snake_length = len(game.snake())
    assert new_snake_length == old_snake_length + 3 + 1 + 0


def test_growth_calls_callback_after_grow_count():
    callback = Mock()
    growth = Cycle(callback, limit=2)
    growth.next()
    callback.assert_not_called()
    growth.next()
    callback.assert_called_once()
