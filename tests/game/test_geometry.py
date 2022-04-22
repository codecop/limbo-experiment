from game.geometry import Point


def test_point_supports_addition():
    assert Point(1, 1) + Point(1, 1) == Point(2, 2)
