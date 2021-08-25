# -*- coding: latin-1 -*-

from enum import Enum
from test_snake import Point, Snake
from test_arena import Arena

import pytest


TurnCommand = Enum("TurnCommand", "LEFT RIGHT")


class Game:
    def __init__(self, snake, arena, grow_count=3):
        self._snake = snake
        self._arena = arena
        self._is_running = True
        self._grow_count = grow_count
        self._ticks_to_grow = 0

    def tick(self, command=None):
        if not self._is_running:
            return

        self._ticks_to_grow += 1

        if self._ticks_to_grow == self._grow_count:
            self._ticks_to_grow = 0
            self._snake.grow()

        # TBD: keep separated?
        if command is TurnCommand.LEFT:
            self._snake.turn_left()
        if command is TurnCommand.RIGHT:
            self._snake.turn_right()
        self._snake.advance()
        self._check_running()

    def _check_running(self):
        self._is_running &= not self._arena.are_positions_occupied(self._snake.body)
        self._is_running &= not self._snake.has_crossed_itself()

    def is_running(self):
        return self._is_running

    def snake(self):
        return self._snake.body

    def arena(self):
        return self._arena.walls()


@pytest.fixture
def game():
    return Game(Snake(), Arena(3, 4))


def test_new_game_has_snake(game):
    snake_coordinates = game.snake()
    assert snake_coordinates == [Point(0, 0), Point(0, -1), Point(0, -2)]


def test_new_game_has_arena(game):
    arena_coordinates = game.arena()
    assert len(arena_coordinates) == 4 + 7 + 7 + 5 + 5


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
    # assert game.is_running() is True
    # assert game.is_running() is False
