# -*- coding: latin-1 -*-

import pytest


class Game:
    pass


@pytest.fixture
def game():
    return Game()


def test_there_is_a_game(game):
    assert game is not None


def test_new_arena_has_snake(game):
    pass
