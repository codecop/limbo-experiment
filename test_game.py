# -*- coding: latin-1 -*-

from test_snake import Point, Snake

import pytest


class Game:
    def __init__(self, snake):
        self._snake = snake

    def snake(self):
        return self._snake.body


@pytest.fixture
def game():
    return Game(Snake())


def test_there_is_a_game(game):
    assert game is not None


def test_new_game_has_snake(game):
    snake_coordinates = game.snake

    # assert snake.body == [Point(0, 0), Point(0, -1), Point(0, -2)]
