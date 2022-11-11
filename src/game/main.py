"""TCR driven Snake Game"""
from tkinter import Tk

from .arena import Arena
from .game import Game
from .presenter import Presenter
from .snake import Snake
from .square_geometry import SquareTiling
from .tkview import TkView


def run():
    # TODO: pull out config (RADIUS, ..., growth rate)
    root = Tk()
    tiling = SquareTiling()  # Tiling defines geometry which gives origin box, directions (left, right), and projection onto pixels
    view = TkView(root, 500, 500)

    snake = Snake(tiling=tiling)
    arena = Arena(box=tiling.box_of(20))
    game = Game(snake, arena, grow_count=3)
    # TODO: window focus
    Presenter(view, game, update_interval=100)
    root.mainloop()
