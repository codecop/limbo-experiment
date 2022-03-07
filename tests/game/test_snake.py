# -*- coding: latin-1 -*-
from game.snake import Point, Directions


def test_there_is_a_snake(snake):
    assert snake.direction == Directions.NORTH
    assert snake.position == Point(0, 0)
    assert snake.body == [Point(0, 0), Point(0, -1), Point(0, -2)]


def test_snake_advances_without_growing(snake):
    snake.advance()
    assert snake.direction == Directions.NORTH
    assert snake.position == Point(0, 1)
    assert snake.body == [Point(0, 1), Point(0, 0), Point(0, -1)]


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
    assert snake.position == Point(0, 1)

    snake.turn_right()
    snake.advance()
    assert snake.position == Point(1, 1)

    snake.turn_right()
    snake.advance()
    assert snake.position == Point(1, 0)

    snake.turn_right()
    snake.advance()
    assert snake.position == Point(0, 0)

    snake.turn_right()
    snake.advance()
    assert snake.position == Point(0, 1)


def test_snake_grows_and_only_once(snake):
    snake.grow()

    snake.advance()
    assert snake.position == Point(0, 1)
    assert snake.body == [Point(0, 1), Point(0, 0), Point(0, -1), Point(0, -2)]

    # and it only grows once -> Code Smell second block in test
    snake.advance()
    assert len(snake.body) == 4


def test_snake_detects_it_has_hit_itself(snake):
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
