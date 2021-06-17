"""
https://docs.google.com/document/d/1ac_DFYlnCyb23le62Tn4I9MRbUnKFIAk9y2lc9wMtR8/edit#heading=h.98eb2udzjo75

Grundanforderungen:
- es startet unten mitte und fÃÂ¤hrt nach oben
- beim Start hat die Schlanke 3 Glieder
- alle n Ticks kommt ein Glied dazu
- jeden Ã¢ÂÂTickÃ¢ÂÂ fÃÂ¤hrt es 1 Feld (und gibt frei)
- auf User Input kann es rechts/links drehen
- trifft Snake sich selbst ist Spiel aus
- trifft Snake eine Wand ist Spiel aus
- Rund um die Arena ist eine Wand

Nice to have
- Es kann ein Labyrint von Datei als Level geladen werden
- Geschwindigkeit
- Schwierigkeitsgrad
- Essen verlÃÂ¤ngert Schlange sofort

Domain
- Snake
  - Direction
  - Length?
  - Head, Tail
  - Ã¢ÂÂAdvanceÃ¢ÂÂ
  - Ã¢ÂÂGrowthÃ¢ÂÂ
- Arena
  - Obstacle
- Tick
- User Input
  - Turn
"""
from enum import Enum

import pytest


class Snake:
    def __init__(self):
        self.direction = "N"
        self.d2 = Directions.NORTH
        self.body = [(0, 0), (0, -1), (0, -2)]

    @property
    def position(self):
        return self.body[0]

    def advance(self):
        if self.direction == "N" or self.d2 == Directions.NORTH:
            new_head = (self.position[0] + 0, self.position[1] + 1)
        self.body = [new_head] + self.body[:-1]

    def turn_right(self):
        right_turns = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.direction = right_turns[self.direction]
        # self.d2 = self.d2.turn_right()


class Direction:
    def __init__(self, name="N", offset=(0, 1)):
        self.name = name
        self.offset = offset

    def offset(self):
        return self.offset


class Directions(Enum):
    NORTH = Direction("N", (0, 1))
    SOUTH = Direction("S", (0, -1))
    EAST = Direction("E", (1, 0))
    WEST = Direction("W", (-1, 0))


@pytest.fixture
def snake():
    return Snake()


def test_there_is_a_snake(snake):
    assert snake.direction == "N"
    assert snake.position == (0, 0)
    assert snake.body == [(0, 0), (0, -1), (0, -2)]


def test_snake_advances_without_growing(snake):
    snake.advance()
    assert snake.direction == "N"
    assert snake.position == (0, 1)
    assert snake.body == [(0, 1), (0, 0), (0, -1)]


def test_snake_rotates(snake):
    snake.turn_right()
    assert snake.direction == "E"
    snake.turn_right()
    assert snake.direction == "S"
    snake.turn_right()
    assert snake.direction == "W"
    snake.turn_right()
    assert snake.direction == "N"
