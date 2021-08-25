# -*- coding: latin-1 -*-

from test_snake import Snake

import pytest


class Game:
    def __init__(self):
        pass


@pytest.fixture
def game():
    return Game()


def test_there_is_a_game(game):
    assert game is not None


def test_new_arena_has_snake(game):
    # snake = game.snake()
    pass
