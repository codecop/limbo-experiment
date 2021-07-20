# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X trifft Snake eine Wand ist Spiel aus
- x Rund um die Arena ist eine Wand

Domain
- Arena
  - Obstacle
"""
from test_snake import Point

import pytest


class Arena:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._walls = []

        self._build_wall()

    def _build_wall(self):
        for x in range(-self._width, self._width + 1):
            self._walls.append(Point(x, -self._height))
            self._walls.append(Point(x, self._height))
        for y in range(-self._height + 1, self._height + 1 - 1):
            self._walls.append(Point(-self._width, y))
            self._walls.append(Point(self._width, y))

    def walls(self):
        return self._walls

    def is_position_occupied(self, position):
        return position in self._walls

    # TODO place_obstacle
    # TODO apple to eat


@pytest.fixture
def arena3x4():
    return Arena(3, 4)


def test_there_is_an_arena_with_walls_around(arena3x4):
    assert Point(-3, -4) in arena3x4.walls()
    # whole left wall
    assert Point(-3, -3) in arena3x4.walls()
    assert Point(-3, -2) in arena3x4.walls()
    assert Point(-3, -1) in arena3x4.walls()
    assert Point(-3, 0) in arena3x4.walls()
    assert Point(-3, 1) in arena3x4.walls()
    assert Point(-3, 2) in arena3x4.walls()
    assert Point(-3, 3) in arena3x4.walls()

    # other corners
    assert Point(-3, 4) in arena3x4.walls()
    assert Point(3, 4) in arena3x4.walls()
    assert Point(3, -4) in arena3x4.walls()

    # BUG!
    assert Point(0, 0) not in arena3x4.walls()
    assert len(arena3x4.walls()) == 4 + 7 + 7 + 5 + 5


def test_if_areana_position_occupied(arena3x4):
    assert arena3x4.is_position_occupied(Point(2, -3)) is False
    assert arena3x4.is_position_occupied(Point(3, -4)) is True
