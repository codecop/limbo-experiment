from test_game import Game
from test_arena import Arena
import pytest
from test_snake import Snake


@pytest.fixture
def snake():
    return Snake()


@pytest.fixture
def arena3x4():
    return Arena(3, 4)


@pytest.fixture
def game():
    return Game(Snake(), Arena(3, 4))
