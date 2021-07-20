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
        pass

    def walls(self):
        return [(-3, -3)]


@pytest.fixture
def arena():
    return Arena(3, 3)


def test_there_is_an_arena_with_walls(arena):
    assert arena.walls()[0] == (-3, -3)
