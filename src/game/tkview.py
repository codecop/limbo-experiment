# -*- coding: latin-1 -*-
"""
TKinter implementation of domain view of game.
* X draw snake
* X draw arena
  * X draw wall
* update/redraw
* ? key commands - könnte auch was anderes sein
* extras
  * game over state
  * display score
  * start new game
  * Tick speed
* "Game Loop" = tick wird scheduled
"""
from tkinter import Tk, Canvas

# registerGameTick, time

# Skipped
# registerViewModel(model)
# update
RADIUS = 5


class TkView:
    def __init__(self, root, width=100, height=100):
        self.window = root
        self.window.title("Snake")
        self._width = width
        self._height = height
        canvas = Canvas(
            root, width=self._width, height=self._height, background="white"
        )
        canvas.pack()
        self.canvas = canvas

        self._snake_objects = {}
        self._arena_objects = {}

    def draw_generic(self, new_points, point_object_mapping, fill, tags):

        old_points = point_object_mapping.keys()

        points_to_add = set(new_points) - set(old_points)
        points_to_remove = set(old_points) - set(new_points)

        # draw new points
        for point in points_to_add:
            point_object_mapping[point] = self.draw_point(point, fill=fill, tags=tags)

        # remove extra points
        for point in points_to_remove:
            self.canvas.delete(point_object_mapping.pop(point))

    def draw_snake(self, new_points):
        self.draw_generic(new_points, self._snake_objects, "green", ("snake"))

    def draw_arena(self, new_points):
        self.draw_generic(new_points, self._arena_objects, "gray", ("arena"))

    def draw_point(self, point, fill, tags):
        xcenter = self._width / 2 + point.x * 2 * RADIUS
        ycenter = self._height / 2 - point.y * 2 * RADIUS
        x0 = xcenter - RADIUS
        x1 = xcenter + RADIUS
        y0 = ycenter - RADIUS
        y1 = ycenter + RADIUS
        return self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, tags=tags)

    def register_left_command(self, callback):
        self.window.bind("<Left>", lambda event: callback())

    def register_right_command(self, callback):
        self.window.bind("<Right>", lambda event: callback())

    def register_start_command(self, callback):
        self.window.bind("<Return>", lambda event: callback())

    def schedule_tick(self, callback, millis):
        # not TDD/TCR because cannot test TKinter scheduling
        self.window.after(millis, callback)

    def game_over(self):
        self.canvas.create_text(
            self._width // 2,
            self._height // 2,
            fill="red",
            text="Game Over!",
            tags=("gameover"),
        )

    def game_start(self):
        self.canvas.create_text(
            self._width // 2,
            self._height // 2,
            fill="blue",
            text="Hit <Return> to start!",
            tags=("gamestart"),
        )


# right and start works ;-)
# arena works ;-)

if __name__ == "__main__":
    root = Tk()
    view = TkView(root)
    root.mainloop()
