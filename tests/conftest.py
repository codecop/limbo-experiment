import os
import sys
import pytest

from game.arena import Arena
from game.game import Game
from game.geometry import Box
from game.snake import Point, Snake


# https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables
# If GITHUB_ACTION is set, we assume we run in a container and can not service user events
skipifcontainer_because_event_handling_not_working = pytest.mark.skipif(
    bool(os.environ.get("GITHUB_ACTION")) or sys.platform.startswith("win"),
    reason="Test not working within GitHub action and on Windows.",
)


@pytest.fixture
def snake():
    return Snake()


@pytest.fixture
def arena3x4():
    return Arena(box=Box(3, 4), initial_apple=Point(0, 1))


@pytest.fixture
def game(snake, arena3x4):
    return Game(snake, arena3x4)


@pytest.fixture
def big_game(snake):
    arena = Arena(box=Box(50, 50), initial_apple=Point(-1, 0))
    return Game(snake, arena, apple_count=10)
