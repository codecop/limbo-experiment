"""
https://docs.google.com/document/d/1ac_DFYlnCyb23le62Tn4I9MRbUnKFIAk9y2lc9wMtR8/edit#heading=h.98eb2udzjo75

Grundanforderungen:
- es startet unten mitte und fÃÂ¤hrt nach oben
- beim Start hat die Schlanke 3 Glieder
- alle n Ticks kommt ein Glied dazu
- jeden Ã¢ÂÂTickÃ¢ÂÂ fÃÂ¤hrt es 1 Feld (und gibt frei)
- auf User Input kann es rechts/links drehen
- trifft Snake sich selbst ist Spiel aus
- trifft Snake eine Wand ist Spiel aus
- Rund um die Arena ist eine Wand

Nice to have
- Es kann ein Labyrint von Datei als Level geladen werden
- Geschwindigkeit
- Schwierigkeitsgrad
- Essen verlÃÂ¤ngert Schlange sofort

Domain
- Snake
  - Direction
  - Length?
  - Head, Tail
  - Ã¢ÂÂAdvanceÃ¢ÂÂ
  - Ã¢ÂÂGrowthÃ¢ÂÂ
- Arena
  - Obstacle
- Tick
- User Input
  - Turn
"""


class Snake:
    def __init__(self):
        self.direction = "N"


def test_there_is_a_snake():
    # this is a change
    snake = Snake()
    assert snake.direction == "N"
