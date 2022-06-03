"""
* Vorgehensmuster prüfen und daneben liegen haben (spez. Coverage Check)
* Axis ist eine Seite von -length bis +length+1 und hat range():Generator oder each() und random()
* Dimension hat 2 Axis und ein randomPoint() und rangeX und rangeY
* Dann verwenden wir das im Arena -> weniger Code dort
* Test für random_free_sample() im Arena fertig implementieren (Random mocken)
* Zuruckgehen und im Game einbauen - wie testen wir?
"""

from game.geometry import Point, Dimension, Axis


def test_point_supports_addition():
    assert Point(1, 2) + Point(3, 4) == Point(4, 6)


def test_dimension():
    dimension = Dimension()


def test_axis():
    axis = Axis(2)
    # TODO: range method, random method
    result = axis.range()
    assert list(result) == [-2, -1, 0, 1, 2]
