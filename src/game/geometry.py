"""
Geometry Objects

The game is grid based and the snake moves into different
directions.

The grid is represented using `Point`.
The snake's direction using `Directions`.
"""
import random
from collections import namedtuple


class Point(namedtuple("Point", ["x", "y"])):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


Direction = namedtuple("Direction", ["name", "offset"])


class Directions:
    NORTH = Direction("N", Point(0, 1))
    EAST = Direction("E", Point(1, 0))
    SOUTH = Direction("S", Point(0, -1))
    WEST = Direction("W", Point(-1, 0))

    @classmethod
    def turn_right(cls, direction):
        _RIGHT = {
            cls.NORTH: cls.EAST,
            cls.EAST: cls.SOUTH,
            cls.SOUTH: cls.WEST,
            cls.WEST: cls.NORTH,
        }

        return _RIGHT[direction]

    @classmethod
    def turn_left(cls, direction):
        _LEFT = {
            cls.NORTH: cls.WEST,
            cls.WEST: cls.SOUTH,
            cls.SOUTH: cls.EAST,
            cls.EAST: cls.NORTH,
        }

        return _LEFT[direction]


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
