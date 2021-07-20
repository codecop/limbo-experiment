# -*- coding: latin-1 -*-
"""
https://docs.google.com/document/d/1ac_DFYlnCyb23le62Tn4I9MRbUnKFIAk9y2lc9wMtR8/edit#heading=h.98eb2udzjo75

Grundanforderungen:
- X es startet unten Mitte und f�hrt nach oben
- X beim Start hat die Schlange 3 Glieder
- alle n Ticks kommt ein Glied dazu
- jeden Tick f�hrt es 1 Feld (und gibt frei)
- auf User Input kann es rechts/links drehen
- trifft Snake sich selbst ist Spiel aus
- trifft Snake eine Wand ist Spiel aus
- Rund um die Arena ist eine Wand

Nice to have
- Es kann ein Labyrint von Datei als Level geladen werden
- Geschwindigkeit
- Schwierigkeitsgrad
- Essen verl�ngert Schlange sofort

Domain
- Snake
  - X Direction
  - ? Length?
  - X Head, Tail (maybe more explicit)
  - X Advance
  - / Growth
- Arena
  - Obstacle
- Tick
- User Input
  - Turn
"""
from collections import namedtuple

import pytest


class Snake:
    def __init__(self):
        self.direction = Directions.NORTH
        self.body = [(0, 0), (0, -1), (0, -2)]

    @property
    def position(self):
        return self.body[0]

    def advance(self):
        new_head = (
            self.position[0] + self.direction.offset[0],
            self.position[1] + self.direction.offset[1],
        )
        self.body = [new_head] + self.body[:-1]

    def turn_right(self):
        self.direction = Directions.turn_right(self.direction)


Direction = namedtuple("Direction", ["name", "offset"])


class Directions:
    NORTH = Direction("N", (0, 1))
    SOUTH = Direction("S", (0, -1))
    EAST = Direction("E", (1, 0))
    WEST = Direction("W", (-1, 0))

    @classmethod
    def turn_right(cls, direction):
        _RIGHT = {
            cls.NORTH: cls.EAST,
            cls.EAST: cls.SOUTH,
            cls.SOUTH: cls.WEST,
            cls.WEST: cls.NORTH,
        }

        return _RIGHT[direction]


@pytest.fixture
def snake():
    return Snake()


def test_there_is_a_snake(snake):
    assert snake.direction == Directions.NORTH
    assert snake.position == (0, 0)
    assert snake.body == [(0, 0), (0, -1), (0, -2)]


def test_snake_advances_without_growing(snake):
    snake.advance()
    assert snake.direction == Directions.NORTH
    assert snake.position == (0, 1)
    assert snake.body == [(0, 1), (0, 0), (0, -1)]


def test_snake_rotates_right(snake):
    snake.turn_right()
    assert snake.direction == Directions.EAST
    snake.turn_right()
    assert snake.direction == Directions.SOUTH
    snake.turn_right()
    assert snake.direction == Directions.WEST
    snake.turn_right()
    assert snake.direction == Directions.NORTH


def test_snake_rotates_left():
    pass


@pytest.mark.skip
def test_snake_moves_in_any_direction():
    pass
