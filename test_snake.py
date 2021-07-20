# -*- coding: latin-1 -*-
"""
https://docs.google.com/document/d/1ac_DFYlnCyb23le62Tn4I9MRbUnKFIAk9y2lc9wMtR8/edit#heading=h.98eb2udzjo75

Grundanforderungen:
- X es startet unten Mitte und fährt nach oben
- X beim Start hat die Schlange 3 Glieder
- X alle n Ticks kommt ein Glied dazu - von aussen gesteuert
- X jeden Tick fährt es 1 Feld (und gibt frei)
- X auf User Input kann es rechts/links drehen - von aussen gesteuert
- trifft Snake sich selbst ist Spiel aus
- trifft Snake eine Wand ist Spiel aus
- Rund um die Arena ist eine Wand

Nice to have
- Es kann ein Labyrint von Datei als Level geladen werden
- Geschwindigkeit
- Schwierigkeitsgrad
- Essen verlängert Schlange sofort

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


def add_elementwise(x, y):
    z = []
    for xi, yi in zip(x, y):
        zi = xi + yi
        z.append(zi)
    return tuple(z)


class Snake:
    def __init__(self):
        self.direction = Directions.NORTH
        self.body = [(0, 0), (0, -1), (0, -2)]
        self._grow = 0

    @property
    def position(self):
        return self.body[0]

    def advance(self):
        # TODO: extend position to support +/-
        advanced_position = add_elementwise(self.position, self.direction.offset)
        if self._grow > 0:
            self._grow -= 1
            whole_body = slice(len(self.body))
            keep_tail = whole_body
        else:
            whole_body_but_last_element = slice(0, -1)
            keep_tail = whole_body_but_last_element

        self.body = [advanced_position] + self.body[keep_tail]

    def turn_right(self):
        self.direction = Directions.turn_right(self.direction)

    def turn_left(self):
        self.direction = Directions.turn_left(self.direction)

    def grow(self):
        self._grow += 1

    def has_crossed_itself(self):
        return self._head() in self._tail()

    def _head(self):
        return self.position

    def _tail(self):
        return self.body[1:]


Direction = namedtuple("Direction", ["name", "offset"])


class Directions:
    NORTH = Direction("N", (0, 1))
    EAST = Direction("E", (1, 0))
    SOUTH = Direction("S", (0, -1))
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

    @classmethod
    def turn_left(cls, direction):
        _RIGHT = {
            cls.NORTH: cls.WEST,
            cls.WEST: cls.SOUTH,
            cls.SOUTH: cls.EAST,
            cls.EAST: cls.NORTH,
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


def test_snake_rotates_left(snake):
    snake.turn_left()
    assert snake.direction == Directions.WEST
    snake.turn_left()
    assert snake.direction == Directions.SOUTH
    snake.turn_left()
    assert snake.direction == Directions.EAST
    snake.turn_left()
    assert snake.direction == Directions.NORTH


def test_snake_moves_in_each_direction(snake):
    snake.advance()
    assert snake.position == (0, 1)

    snake.turn_right()
    snake.advance()
    assert snake.position == (1, 1)

    snake.turn_right()
    snake.advance()
    assert snake.position == (1, 0)

    snake.turn_right()
    snake.advance()
    assert snake.position == (0, 0)

    snake.turn_right()
    snake.advance()
    assert snake.position == (0, 1)


def test_snake_grows_and_only_once(snake):
    snake.grow()

    snake.advance()
    assert snake.position == (0, 1)
    assert snake.body == [(0, 1), (0, 0), (0, -1), (0, -2)]

    # and it only grows once -> Code Smell second block in test
    snake.advance()
    assert len(snake.body) == 4


def test_snake_has_hit_itself(snake):
    snake.grow()
    snake.grow()

    assert snake.has_crossed_itself() is False

    snake.turn_right()
    snake.advance()

    assert snake.has_crossed_itself() is False

    snake.turn_right()
    snake.advance()

    assert snake.has_crossed_itself() is False

    snake.turn_right()
    snake.advance()

    assert snake.has_crossed_itself() is True
