# -*- coding: latin-1 -*-

from enum import Enum
from test_snake import Point, Snake
from test_arena import Arena

import pytest


TurnCommand = Enum("TurnCommand", "LEFT RIGHT")


class Game:
    def __init__(self, snake, arena):
        self._snake = snake
        self._arena = arena

    def tick(self, command=None):
        # TBD: keep separated?
        if command is TurnCommand.LEFT:
            self._snake.turn_left()
        if command is TurnCommand.RIGHT:
            self._snake.turn_right()
        self._snake.advance()

    def is_running(self):
        # TODO: different cases
        return not self._arena.are_positions_occupied(self._snake.body)

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


def test_if_snake_hits_itself_game_is_over(game):
    pass


def test_if_game_is_over_stop_advancing_snake(game):
    pass
