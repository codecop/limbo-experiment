from tkinter import Tk

from test_arena import Arena
from test_game import Game
from test_presenter import Presenter
from test_snake import Snake
from test_tk_view import TkView

if __name__ == "__main__":
    # TODO: pull out config (RADIUS, width, size, ..., growth rate, schedule interval)
    root = Tk()
    view = TkView(root, 500, 500)

    snake = Snake()
    arena = Arena(20, 20)
    game = Game(snake, arena)

    Presenter(view, game)
    root.mainloop()
