"""
Method one: the head fake. When you create your app,
don't put all the widgets in the root window.
Instead, hide the root window and create a new toplevel
that represents your application.
When you restart it's just a matter of destroying that new toplevel
and re-running all your start-up logic.

Links:
* https://stackoverflow.com/questions/731887/resetting-the-main-gui-window
* https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application/17470842#17470842
"""
# -*- coding: latin-1 -*-
import _tkinter
import tkinter as tk
import pytest
from unittest.mock import Mock

from conftest import (
    skipifcontainer_because_event_handling_not_working,
)  # TODO: resolve differently

from game.snake import Point
from game.tkview import RADIUS, TkView


@pytest.fixture(scope="module")
def hidden_root():
    """Create hidden root window for reuse across tests."""
    root = tk.Tk()
    root.withdraw()
    return root


@pytest.fixture
def fresh_toplevel(hidden_root):
    """Create new toplevel window on top of root."""
    toplevel = tk.Toplevel(hidden_root)
    yield toplevel
    toplevel.destroy()  # TBD: Need this setup for test involving `handle_events`.


def handle_events(window):
    # used in conjunction with a single toplevel window
    # we need to access root, i.e. master, to handle events
    while window.master.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
        pass


@pytest.fixture
def view(fresh_toplevel):
    return TkView(fresh_toplevel)


def test_window_title_is_snake(view):
    assert view.window.title() == "Snake"


def test_game_start_draws_message(view):
    view.game_start()
    items = view.canvas.find_withtag("gamestart")
    assert 1 == len(items)


def test_game_over_draws_message(view):
    view.game_over()
    items = view.canvas.find_withtag("gameover")
    assert 1 == len(items)


@skipifcontainer_because_event_handling_not_working
def test_command_key_left_triggers_associated_callback(fresh_toplevel):
    view = TkView(fresh_toplevel)
    handle_events(fresh_toplevel)
    callback = Mock()

    view.register_left_command(callback)
    view.window.event_generate("<Left>")

    callback.assert_called_once()
    # handle_events(fresh_toplevel)  # TBD: Unclear. We need it above but not here. Why?


def test_view_draws_snake(view):
    view.draw_snake([Point(0, 0), Point(1, 2)])
    items = view.canvas.find_withtag("snake")
    assert 2 == len(items)

    item_coords = [view.canvas.coords(item) for item in items]
    assert [45, 45, 55, 55] in item_coords
    assert [
        45 + 2 * RADIUS,
        45 - 4 * RADIUS,
        55 + 2 * RADIUS,
        55 - 4 * RADIUS,
    ] in item_coords


def test_draw_same_snake_twice_draws_only_once(view):
    view.draw_snake([Point(0, 0), Point(1, 2)])
    view.draw_snake([Point(0, 0), Point(1, 2)])
    items = view.canvas.find_withtag("snake")
    assert 2 == len(items)


def test_draw_new_snake_removes_old_snake(view):
    view.draw_snake([Point(0, 0), Point(1, 2)])
    view.draw_snake([Point(1, 0), Point(0, 0)])
    items = view.canvas.find_withtag("snake")
    assert 2 == len(items)


def test_draw_apple(view):
    view.draw_apples([Point(0, 0), Point(1, 2)])
    items = view.canvas.find_withtag("apple")
    assert 2 == len(items)


# right and start works ;-)
# arena works ;-)


if __name__ == "__main__":
    # exemplary view
    root = tk.Tk()
    TkView(root)
    root.mainloop()

    # exemplary test setup
    import tkinter as tk

    hidden_root_window = tk.Tk()
    hidden_root_window.title("Hidden root <-- we will never see it ;)")
    hidden_root_window.withdraw()

    actual_window = tk.Toplevel(hidden_root_window)
    actual_window.title("We use this!")

    # actual_window.mainloop()
    hidden_root_window.mainloop()  # Kill the root to close all
