# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X trifft Snake eine Wand ist Spiel aus
- X Rund um die Arena ist eine Wand

Domain
- Arena
  - Obstacle
"""


class Arena:
    def __init__(self, box):
        self._box = box
        self._walls = set()
        self._apples = []

        self._build_wall()

    def _build_wall(self):
        # TODO NEXT move logic into box, tiling gives us proper box then
        walls = self._box.boundary_points()
        self._walls = self._walls.union(walls)

    def place_apple(self, apple):
        self._apples.append(apple)

    def walls(self):
        return self._walls

    def apples(self):
        return self._apples

    def is_position_wall(self, position):
        return position in self._walls

    def are_positions_wall(self, positions):
        return any(self.is_position_wall(position) for position in positions)

    def is_position_apple(self, position):
        return position in self._apples

    def is_position_occupied(self, candidate_free_point):
        # fmt:off
        return self.is_position_wall(candidate_free_point) or \
            self.is_position_apple(candidate_free_point)
        # fmt:on

    def remove_apple(self, position):
        self._apples.remove(position)

    def sample_free_point(self):
        candidate_free_point = self._box.random_point()
        while self.is_position_occupied(candidate_free_point):
            candidate_free_point = self._box.random_point()
            # TODO (ignore) stop loop on full arena
        return candidate_free_point


# Arena is complete
# TODO later: place_obstacle
