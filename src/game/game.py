# -*- coding: latin-1 -*-
from enum import Enum

from .geometry import Point

TurnCommand = Enum("TurnCommand", "LEFT RIGHT")


class Game:
    def __init__(self, snake, arena, grow_count=3, apple_count=20):
        self._snake = snake
        self._arena = arena
        self._is_running = True
        # self._snake_growth_counter = Cycle(counter=3, call=self._snake.grow)
        # self._snake_growth_counter.next()
        self._snake_growth = Cycle(limit=grow_count, callback=self._snake.grow)
        self._apple_count = apple_count
        self._ticks_to_apple = 0

    def tick(self, command=None):
        if not self._is_running:
            return
        self._snake_growth.handle()  # self._snake.grow
        self._handle_command(command)
        self._snake.advance()
        if self._arena.is_position_apple(self._snake.position):
            self._snake.grow()
            self._arena.remove_apple(self._snake.position)
        self._handle_apple_growth()
        self._check_running()

    def _handle_apple_growth(self):
        self._ticks_to_apple += 1
        if self._ticks_to_apple == self._apple_count:
            self._ticks_to_apple = 0
            candidate_apple = Point(-1, -1)
            while self._arena.is_position_apple(candidate_apple):
                # TODO: create apple at suitable position
                # generate random position within walls
                # cf Arena._build_wall for suitable x and y ranges
                # check if already is apple or snake, if so then skip
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


class Cycle:
    def __init__(self, limit=1, callback=None):
        self._limit = limit
        self._count = 0
        self._callback = callback

    def handle(self):
        self._count += 1
        if self._count == self._limit:
            self._count = 0
            self._callback()
