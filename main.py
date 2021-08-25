from tkinter import Tk
from test_presenter import Presenter
from test_tk_view import TkView

if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    Presenter(view, game)
    root.mainloop()
