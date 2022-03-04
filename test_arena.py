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
        self._apples = []

        self._build_wall()
        self._set_apple()

    def _build_wall(self):
        for x in range(-self._width, self._width + 1):
            self._walls.append(Point(x, -self._height))
            self._walls.append(Point(x, self._height))
        for y in range(-self._height + 1, self._height + 1 - 1):
            self._walls.append(Point(-self._width, y))
            self._walls.append(Point(self._width, y))

    def _set_apple(self):
        self._apples = [Point(0,0)]

    def walls(self):
        return self._walls

    def is_position_occupied(self, position):
        return position in self._walls

    def are_positions_occupied(self, positions):
        return any(self.is_position_occupied(position) for position in positions)

    def is_position_apple(self, position):
        return position in self._apples

    # TODO later: place_obstacle
    # TODO later: place apple to eat


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


def test_if_arena_positions_are_occupied(arena3x4):
    assert arena3x4.are_positions_occupied([Point(2, -3), Point(3, -4)]) is True

def test_area_has_apple(arena3x4):
    assert arena3x4.is_position_apple(Point(0, 0)) is True
    pass
