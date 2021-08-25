from test_presenter import Presenter


if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    game = Presenter(view)
    root.mainloop()
