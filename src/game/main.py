"""TCR driven Snake Game"""

from tkinter import Tk

from game.arena import Arena
from game.game import Game
from game.presenter import Presenter
from game.snake import Snake
from game.tkview import TkView

if __name__ == "__main__":
    # TODO: pull out config (RADIUS, ..., growth rate)
    # TODO: add as entry point
    root = Tk()
    view = TkView(root, 500, 500)

    snake = Snake()
    arena = Arena(20, 20)
    game = Game(snake, arena)
    # TODO: window focus
    Presenter(view, game, update_interval=100)
    root.mainloop()
