# -*- coding: latin-1 -*-
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


def test_if_areana_position_occupied(arena3x4):
    assert arena3x4.is_position_wall(Point(2, -3)) is False
    assert arena3x4.is_position_wall(Point(3, -4)) is True


def test_if_arena_positions_are_occupied(arena3x4):
    assert arena3x4.are_positions_wall([Point(2, -3), Point(3, -4)]) is True


def test_arena_has_apple(arena3x4):
    assert arena3x4.is_position_apple(Point(0, 1)) is True


def test_arena_can_remove_apple(arena3x4):
    arena3x4.remove_apple(Point(0, 1))
    assert arena3x4.is_position_apple(Point(0, 1)) is False


def test_arena_apples(arena3x4):
    assert arena3x4.apples() == [Point(0, 1)]


def test_arena_creates_random_point_not_on_wall():
    arena = Arena(Box(1, 2))
    point = arena.sample_free_point()
    assert not arena.is_position_wall(point)
    assert point in [Point(0, 1), Point(0, 0), Point(0, -1)]


def test_arena_creates_random_point_not_on_apple():
    arena = Arena(Box(1, 2))
    arena.place_apple(Point(0, 0))
    arena.place_apple(Point(0, -1))
    point = arena.sample_free_point()
    assert point == Point(0, 1)
    assert not arena.is_position_apple(point)
    assert not arena.is_position_wall(point)


def test_arena_creates_random_point_not_place():
    arena = Arena(Box(1, 1))
    arena.place_apple(Point(0, 0))
    # point = arena.sample_free_point()
    # assert point is None
