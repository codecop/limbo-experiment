# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- trifft Snake eine Wand ist Spiel aus
- Rund um die Arena ist eine Wand

Domain
- Arena
  - Obstacle
"""
from collections import namedtuple

import pytest


class Arena:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def walls(self):
        return [(-self._width, -self._height)]


@pytest.fixture
def arena3x4():
    return Arena(3, 4)


def test_there_is_an_arena_with_walls(arena3x4):
    assert arena3x4.walls()[0] == (-3, -4)
