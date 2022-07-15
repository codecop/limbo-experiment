# -*- coding: latin-1 -*-
import pytest
from game.arena import Arena
from game.geometry import Box, Point


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

