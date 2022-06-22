# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X trifft Snake eine Wand ist Spiel aus
- x Rund um die Arena ist eine Wand

Domain
- Arena
  - Obstacle
"""
from .geometry import Point


class Arena:
    def __init__(self, box, initial_apple=None):
        self._box = box
        self._walls = set()
        self._apples = []

        self._build_wall()
        self.place_apple(initial_apple)

    def _build_wall(self):
        for x in self._box.x.range():
            self._walls.add(Point(x, self._box.y.min()))
            self._walls.add(Point(x, self._box.y.max()))
        for y in self._box.y.range():
            self._walls.add(Point(self._box.x.min(), y))
            self._walls.add(Point(self._box.x.max(), y))

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
