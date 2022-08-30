# -*- coding: latin-1 -*-
"""
* Dann verwenden wir das im Arena -> weniger Code dort
* Test für random_free_sample() im Arena fertig implementieren (Random mocken)
* Zurückgehen und im Game einbauen - wie testen wir?
"""
import pytest

from game.square_geometry import Directions, Point, Box, Axis


def test_point_supports_addition():
    assert Point(1, 2) + Point(3, 4) == Point(4, 6)


@pytest.mark.parametrize("execution_number", range(100))
def test_box_random_point(execution_number):
    box = Box(width=2, height=3)
    point = box.random_point()
    assert -2 <= point.x <= 2 and -3 <= point.y <= 3


def test_axis_range():
    axis = Axis(2)
    result = axis.range()
    assert list(result) == [-2, -1, 0, 1, 2]


def test_axis_min():
    axis = Axis(4)
    assert axis.min() == -4


def test_axis_max():
    axis = Axis(3)
    assert axis.max() == 3


@pytest.mark.parametrize("execution_number", range(100))
def test_axis_random(execution_number):
    axis = Axis(2)
    result = axis.random()
    assert -2 <= result <= 2


@pytest.mark.parametrize(
    "current,opposition",
    [(Directions.NORTH, Directions.SOUTH), (Directions.EAST, Directions.WEST)],
)
def test_opposite_direction(current, opposition):
    assert current.opposite() == opposition
    assert opposition.opposite() == current


def test_project_point():
    pass


def test_point_transformer():
    pass
