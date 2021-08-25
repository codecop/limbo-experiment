# -*- coding: latin-1 -*-

from test_snake import Point, Snake
from test_arena import Arena

import pytest


class Game:
    def __init__(self, snake, arena=None):
        self._snake = snake

    def snake(self):
        return self._snake.body


@pytest.fixture
def game():
    return Game(Snake())


def test_there_is_a_game(game):
    assert game is not None


def test_new_game_has_snake(game):
    snake_coordinates = game.snake()
    assert snake_coordinates == [Point(0, 0), Point(0, -1), Point(0, -2)]


def test_new_game_has_arena(game):
    pass
