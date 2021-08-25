from test_game import Game
from test_arena import Arena
from test_snake import Snake
from tkinter import Tk
from test_presenter import Presenter
from test_tk_view import TkView

if __name__ == "__main__":
    root = Tk()
    view = TkView(root)

    snake = Snake()
    arena = Arena(3, 4)
    game = Game(snake, arena)

    Presenter(view, game)
    root.mainloop()
