from tkinter import TK
from test_presenter import Presenter
from test_tk_view import TkView

if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    game = Presenter(view)
    root.mainloop()
