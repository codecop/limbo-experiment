# -*- coding: latin-1 -*-
from game.geometry import Point


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


def test_arena_has_apple(arena3x4):
    assert arena3x4.is_position_apple(Point(0, 1)) is True


def test_arena_can_remove_apple(arena3x4):
    arena3x4.remove_apple(Point(0, 1))
    assert arena3x4.is_position_apple(Point(0, 1)) is False


def test_arena_apples(arena3x4):
    assert arena3x4.apples() == [Point(0, 1)]


def test_arena_creates_random_point(arena3x4):
    point = arena3x4.sample_free_point()
    assert point != Point(0, 1)  # <-- initial apple
    assert not arena3x4.is_position_occupied(point)
