# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X es startet unten Mitte und f�hrt nach oben
- X beim Start hat die Schlange 3 Glieder
- X alle n Ticks kommt ein Glied dazu - von aussen gesteuert
- X jeden Tick f�hrt es 1 Feld (und gibt frei)
- X auf User Input kann es rechts/links drehen - von aussen gesteuert
- X trifft Snake sich selbst ist Spiel aus - von aussen gesteuert
- X trifft Snake eine Wand ist Spiel aus - von aussen gesteuert
- X Rund um die Arena ist eine Wand

Nice to have
- Es kann ein Labyrinth von Datei als Level geladen werden
- Geschwindigkeit
- Schwierigkeitsgrad
- X Essen verl�ngert Schlange sofort

Domain
- Snake
  - X Direction
  - ? Length?
  - X Head, Tail (maybe more explicit)
  - X Advance
  - X Growth
- Arena
  - Obstacle
- Game?
  - X Tick
- User Input/UI
  - X Game Loop
  - X Turn
"""
from .geometry import Directions, SquareTiling


class Snake:
    def __init__(self, tiling: SquareTiling):
        self.direction = tiling.starting_direction()
        center = tiling.origin()
        second = center - self.direction.offset  # Point(0, -1)
        third = second - self.direction.offset  # Point(0, -2)
        self.body = [center, second, third]
        self._times_to_grow = 0

    @property
    def position(self):
        return self.body[0]

    def advance(self):
        advanced_position = self.position + self.direction.offset
        if self._is_growing():
            self._times_to_grow -= 1
            whole_body = slice(len(self.body))
            keep_tail = whole_body
        else:
            whole_body_but_last_element = slice(0, -1)
            keep_tail = whole_body_but_last_element

        self.body = [advanced_position] + self.body[keep_tail]

    def _is_growing(self):
        return self._times_to_grow > 0

    def turn_right(self):
        self.direction = Directions.turn_right(self.direction)

    def turn_left(self):
        self.direction = Directions.turn_left(self.direction)

    def grow(self):
        self._times_to_grow += 1

    def has_crossed_itself(self):
        return self._head() in self._tail()

    def _head(self):
        return self.position

    def _tail(self):
        return self.body[1:]


# Snake is complete
