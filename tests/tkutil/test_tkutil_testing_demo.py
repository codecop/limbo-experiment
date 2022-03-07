import tkinter as tk
from tkutil.testing import TkinterTestCase
from conftest import (
    skipifcontainer_because_event_handling_not_working,
)  # TODO: resolve differently


class ExampleApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent  # not needed
        self.create_widgets()
        self.value = None
        self.parent.bind("<Return>", self.save)

    def create_widgets(self):
        self.label = tk.Label(self, text=u"Value:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Ok", command=self.save)
        self.button.pack()

        self.entry.focus_set()

    def save(self, *_):
        self.value = self.entry.get()
        print(self.value)


def example_main():
    root = tk.Tk()
    root.title("App is a Frame")
    app = ExampleApplication(root)
    app.pack()
    root.mainloop()


class ExampleApplicationThatIsNotAFrame:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Is not a frame")
        self.create_widgets()
        self.value = None
        self.parent.bind("<Return>", self.save)

    def create_widgets(self):
        self.label = tk.Label(self.parent, text=u"Value:")
        self.label.pack()
        self.entry = tk.Entry(self.parent)
        self.entry.pack()
        self.button = tk.Button(self.parent, text="Ok", command=self.save)
        self.button.pack()

        self.entry.focus_set()

    def save(self, *_):
        self.value = self.entry.get()
        print(self.value)


def examplethatisnotaframe_main():
    root = tk.Tk()
    app = ExampleApplicationThatIsNotAFrame(root)
    root.mainloop()


@skipifcontainer_because_event_handling_not_working
class TestExampleApplication(TkinterTestCase):
    def test_application_that_is_a_frame(self):
        app = ExampleApplication(self.root)
        app.pack()
        self.update_gui()
        app.entry.insert(0, "Entered text")
        app.entry.event_generate("<Return>")

        # self.update_gui()  # why don't we need this one?
        self.assertEqual(app.value, "Entered text")

    def test_application_that_is_not_a_frame(self):
        app = ExampleApplicationThatIsNotAFrame(self.root)
        self.update_gui()
        app.entry.insert(0, "Entered text")
        app.entry.event_generate("<Return>")
        # self.update_gui()  # why don't we need this one?

        self.assertEqual(app.value, "Entered text")


if __name__ == "__main__":
    example_main()
    # examplethatisnotaframe_main()
