# -*- coding: latin-1 -*-
"""
Grundanforderungen:
- X alle n Ticks kommt ein Glied dazu - von aussen gesteuert
- X auf User Input kann es rechts/links drehen - von aussen gesteuert
- X trifft Snake sich selbst ist Spiel aus - von aussen gesteuert
- X trifft Snake eine Wand ist Spiel aus - von aussen gesteuert
"""
from .game import TurnCommand

# create game: create Arena, create Snake, get View
# right/left pressed
# tick = draw on view
# game ended!


class Presenter:
    def __init__(self, view, game, update_interval=100):
        self._view = view
        self._game = game
        self._next_command = None
        self._update_interval = update_interval

        self._register_command_callbacks(view)

    def _register_command_callbacks(self, view):
        view.register_start_command(self.start)
        view.register_left_command(self.left)
        view.register_right_command(self.right)

    def left(self):
        self._next_command = TurnCommand.LEFT

    def right(self):
        self._next_command = TurnCommand.RIGHT

    def _loop(self):
        self._game.tick(self._next_command)
        self._next_command = None

        if self._game.is_running():
            self.start()
        else:
            self._view.game_over()

    def _draw(self):
        self._view.draw_snake(self._game.snake())
        self._view.draw_arena(self._game.arena())
        self._view.draw_apples(self._game.apples())

    def start(self):
        self._draw()
        self._view.schedule_tick(self._loop, self._update_interval)
