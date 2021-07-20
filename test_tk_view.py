# -*- coding: latin-1 -*-
"""
TKinter implementation of domain view of game.
* draw snake
* draw arena
  * draw wall
* update/redraw
* ? key commands - könnte auch was anderes sein
* extras
  * game over state
  * display score
  * start new game
  * Tick speed
* "Game Loop" = tick wird scheduled
"""
from test_snake import Point

from tkinter import Tk, Canvas
from tkinter_snippets.test_util import TkinterTestCase

import pytest

# registerGameTick, time
# register cursorr keys callback

# print_snake(points)
# print_arena(points)

# registerViewModel(model)
# update


@pytest.fixture
def view():
    return 1


def test_view_draws_snake(view):
    # view.draw_snake([(1,1), (2,1), (3,1)])
    # assertThatUiHasBluePixelAt(100,100)
    pass


class TestTkView(TkinterTestCase):
    def test_window_title_is_snake(self):
        pass
