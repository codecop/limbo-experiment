"""
* Dann verwenden wir das im Arena -> weniger Code dort
* Test für random_free_sample() im Arena fertig implementieren (Random mocken)
* Zuruckgehen und im Game einbauen - wie testen wir?
"""
import pytest

from game.geometry import Point, Dimension, Axis


def test_point_supports_addition():
    assert Point(1, 2) + Point(3, 4) == Point(4, 6)


def test_dimension_rangex():
    dimension = Dimension(width=2, height=3)
    result = dimension.range_x()
    assert list(result) == [-2, -1, 0, 1, 2]


def test_dimension_rangey():
    dimension = Dimension(width=2, height=3)
    result = dimension.range_y()
    assert list(result) == [-3, -2, -1, 0, 1, 2, 3]


@pytest.mark.parametrize("execution_number", range(100))
def test_dimension_random_point(execution_number):
    dimension = Dimension(width=2, height=3)
    point = dimension.random_point()
    assert -2 <= point.x <= 2 and -3 <= point.y <= 3


def test_axis_range():
    axis = Axis(2)
    result = axis.range()
    assert list(result) == [-2, -1, 0, 1, 2]


def test_axis_min():
    axis = Axis(2)
    assert axis.min() == -2


def test_axis_max():
    axis = Axis(3)
    assert axis.max() is None


@pytest.mark.parametrize("execution_number", range(100))
def test_axis_random(execution_number):
    axis = Axis(2)
    result = axis.random()
    assert -2 <= result <= 2
