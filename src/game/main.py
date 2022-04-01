"""TCR driven Snake Game"""
from tkinter import Tk

from .arena import Arena
from .game import Game
from .presenter import Presenter
from .snake import Snake
from .tkview import TkView


def run():
    # TODO: pull out config (RADIUS, ..., growth rate)
    root = Tk()
    view = TkView(root, 500, 500)

    snake = Snake()
    arena = Arena(20, 20)
    game = Game(snake, arena)
    # TODO: window focus
    Presenter(view, game, update_interval=100)
    root.mainloop()
