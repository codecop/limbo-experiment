# -*- coding: latin-1 -*-
from enum import Enum

from game.snake import Point

TurnCommand = Enum("TurnCommand", "LEFT RIGHT")


class Game:
    def __init__(self, snake, arena, grow_count=3, apple_count=20):
        self._snake = snake
        self._arena = arena
        self._is_running = True
        self._grow_count = grow_count
        self._ticks_to_grow = 0
        self._apple_count = apple_count
        self._ticks_to_apple = 0

    def tick(self, command=None):
        if not self._is_running:
            return
        self._handle_growth()
        self._handle_command(command)
        self._snake.advance()
        if self._arena.is_position_apple(self._snake.position):
            self._snake.grow()
            self._arena.remove_apple(self._snake.position)
        self._handle_apple_growth()
        self._check_running()

    def _handle_growth(self):
        self._ticks_to_grow += 1
        if self._ticks_to_grow == self._grow_count:
            self._ticks_to_grow -= self._grow_count
            self._snake.grow()

    def _handle_apple_growth(self):
        self._ticks_to_apple += 1
        if self._ticks_to_apple == self._apple_count:
            self._ticks_to_apple -= self._apple_count
            candidate_apple = Point(-1, -1)
            while self._arena.is_position_apple(candidate_apple):
                # TODO: create apple at suitable position
                # generate random position within walls
                # check if already is apple or snake, then skip
                candidate_apple = Point(candidate_apple.x + 1, candidate_apple.y + 1)
            self._arena.place_apple(candidate_apple)

    def _handle_command(self, command):
        if command is TurnCommand.LEFT:
            self._snake.turn_left()
        if command is TurnCommand.RIGHT:
            self._snake.turn_right()

    def _check_running(self):
        self._is_running &= not self._arena.are_positions_occupied(self._snake.body)
        self._is_running &= not self._snake.has_crossed_itself()

    def is_running(self):
        return self._is_running

    def snake(self):
        return self._snake.body

    def arena(self):
        return self._arena.walls()

    def apples(self):
        return self._arena.apples()
