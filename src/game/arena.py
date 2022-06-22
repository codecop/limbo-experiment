# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X trifft Snake eine Wand ist Spiel aus
- x Rund um die Arena ist eine Wand

Domain
- Arena
  - Obstacle
"""
from .geometry import Dimension, Point


class Arena:
    def __init__(self, width, height, initial_apple=Point(0, 1)):
        self._width = width
        self._height = height
        self._dimension = Dimension(width, height)
        self._walls = set()
        self._apples = []

        self._build_wall()
        self.place_apple(initial_apple)

    def _build_wall(self):
        for x in self._dimension.x.range():
            self._walls.add(Point(x, self._dimension.y.min()))
            self._walls.add(Point(x, self._dimension.y.max()))
        for y in self._dimension.range_y():
            self._walls.add(Point(self._dimension.x.min(), y))
            self._walls.add(Point(self._dimension.x.max(), y))

    def place_apple(self, apple):
        self._apples.append(apple)

    def walls(self):
        return self._walls

    def apples(self):
        return self._apples

    def is_position_occupied(self, position):
        return position in self._walls

    def are_positions_occupied(self, positions):
        return any(self.is_position_occupied(position) for position in positions)

    def is_position_apple(self, position):
        return position in self._apples

    def remove_apple(self, position):
        self._apples.remove(position)

    def sample_free_point(self):
        candidate_free_point = Point(1, 1)
        return candidate_free_point

    # TODO later: place_obstacle
