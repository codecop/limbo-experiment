"""
Geometry Objects

The game is grid based and the snake moves into different
directions.

The grid is represented using `Point`.
The snake's direction using `Directions`.
"""
import random
from collections import namedtuple


class SquareTiling:
    def starting_direction(self):
        return Directions.NORTH

    def origin(self):
        return Point(0, 0)


class Point(namedtuple("Point", ["x", "y"])):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


Direction = namedtuple("Direction", ["name", "offset"])


def _direction_opposite(direction):
    _OPPOSITE = {
        Directions.NORTH: Directions.SOUTH,
    }
    return _OPPOSITE[direction]


def _direction_turn_right(self):
    _RIGHT = {
        Directions.NORTH: Directions.EAST,
        Directions.EAST: Directions.SOUTH,
        Directions.SOUTH: Directions.WEST,
        Directions.WEST: Directions.NORTH,
    }

    return _RIGHT[self]


def turn_left(self):
    _LEFT = {
        Directions.NORTH: Directions.WEST,
        Directions.WEST: Directions.SOUTH,
        Directions.SOUTH: Directions.EAST,
        Directions.EAST: Directions.NORTH,
    }

    return _LEFT[self]


Direction.opposite = _direction_opposite
Direction.turn_right = _direction_turn_right
Direction.turn_left = turn_left
# NEXT: Implement opposite as class method using a lookup table


class Directions:
    NORTH = Direction("N", Point(0, 1))
    EAST = Direction("E", Point(1, 0))
    SOUTH = Direction("S", Point(0, -1))
    WEST = Direction("W", Point(-1, 0))


class Box:
    def __init__(self, width, height):
        self.x = Axis(width)
        self.y = Axis(height)

    def random_point(self):
        return Point(self.x.random(), self.y.random())


class Axis:
    def __init__(self, length):
        self._length = length

    def range(self):
        return range(self.min(), self.max() + 1)

    def random(self):
        return random.randint(self.min(), self.max())

    def min(self):
        return -self._length

    def max(self):
        return self._length
