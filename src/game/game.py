# -*- coding: latin-1 -*-
from enum import Enum

from game.snake import Snake

TurnCommand = Enum("TurnCommand", "LEFT RIGHT")


class Game:
    def __init__(self, snake: Snake, arena, grow_count=3, apple_count=20):
        self._snake = snake
        self._arena = arena
        self._is_running = True
        self._snake_growth_counter = Cycle(self._snake.grow, limit=grow_count)
        self._apple_placement_counter = Cycle(self._place_apple, limit=apple_count)

    def tick(self, command=None):
        if not self._is_running:
            return
        self._snake_growth_counter.next()
        self._handle_command(command)
        self._snake.advance()
        if self._arena.is_position_apple(self._snake.position):
            self._snake.grow()
            self._arena.remove_apple(self._snake.position)
        self._apple_placement_counter.next()
        self._check_running()

    def _place_apple(self):
        candidate_apple = self._arena.sample_free_point()
        while candidate_apple in self._snake.body:
            candidate_apple = self._arena.sample_free_point()
        # TODO: create apple at suitable position
        # check if already is snake, if so then skip
        self._arena.place_apple(candidate_apple)

    def _handle_command(self, command):
        if command is TurnCommand.LEFT:
            self._snake.turn_left()
        if command is TurnCommand.RIGHT:
            self._snake.turn_right()

    def _check_running(self):
        self._is_running &= not self._arena.are_positions_wall(self._snake.body)
        self._is_running &= not self._snake.has_crossed_itself()

    def is_running(self):
        return self._is_running

    def snake(self):
        return self._snake.body

    def arena(self):
        return self._arena.walls()

    def apples(self):
        return self._arena.apples()


class Cycle:
    def __init__(self, callback, limit=1):
        self._limit = limit
        self._count = 0
        self._callback = callback

    def next(self):
        self._count += 1
        if self._count == self._limit:
            self._count = 0
            self._callback()
