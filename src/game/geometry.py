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


class Direction(namedtuple("Direction", ["name", "offset"])):
    def opposite(self):
        _OPPOSITE = {
            Directions.NORTH: Directions.SOUTH,
            Directions.EAST: Directions.WEST,
            Directions.SOUTH: Directions.NORTH,
            Directions.WEST: Directions.EAST,
        }
        return _OPPOSITE[self]

    def turn_right(self):
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

    def boundary_points(self):
        walls = set()
        for x in self.x.range():
            walls.add(Point(x, self.y.min()))
            walls.add(Point(x, self.y.max()))
        for y in self.y.range():
            walls.add(Point(self.x.min(), y))
        return walls


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
