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
    def walls(self):
        return [(-3, -3)]


@pytest.fixture
def arena():
    return Arena()


def test_there_is_an_arena_with_walls(arena):
    pass
    # assert arena.walls()[0] == (-3,-3)
