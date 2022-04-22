from game.geometry import Point


def test_point_supports_addition():
    assert Point(1, 2) + Point(3, 4) == Point(4, 6)
