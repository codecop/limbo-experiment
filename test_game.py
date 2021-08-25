# -*- coding: latin-1 -*-

from test_snake import Point, Snake
from test_arena import Arena

import pytest


class Game:
    def __init__(self, snake, arena):
        self._snake = snake
        self._arena = arena

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
