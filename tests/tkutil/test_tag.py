# -*- coding: latin-1 -*-
"""
Snippet showing how to find items on a canvas using tags.
"""
from tkinter import Tk, Canvas
from tkutil.testing import TkinterTestCase


def create_canvas_with_items(root):
    root.title("Canvas objects with tags")
    root.resizable(False, False)

    canvas = Canvas(root, width=100, height=100, background="white")
    canvas.pack()

    canvas.create_rectangle(10, 10, 20, 20, fill="red", tags=("rectangle", "r-1"))
    canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags=("rectangle", "r-2"))
    canvas.create_oval(40, 40, 80, 80, fill="green", tags=("oval",))
    return canvas


class TestFindItemsUsingTags(TkinterTestCase):
    def test_find_withtag_and_assert_properties(self):
        canvas = create_canvas_with_items(self.root)
        self.update_gui()

        items = canvas.find_withtag("rectangle")
        assert 2 == len(items)

        items = canvas.find_withtag("r")
        assert 0 == len(items)

        rectangle_one = canvas.find_withtag("r-1")
        assert [10, 10, 20, 20] == canvas.coords(rectangle_one)


if __name__ == "__main__":
    root = Tk()
    canvas = create_canvas_with_items(root)
    root.mainloop()
