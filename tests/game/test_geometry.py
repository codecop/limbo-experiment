from game.geometry import Point, Dimension, Axis


def test_point_supports_addition():
    assert Point(1, 2) + Point(3, 4) == Point(4, 6)


def test_dimension():
    dimension = Dimension()


def test_axis():
    axis = Axis()
