# -*- coding: latin-1 -*-
"""
Snippet showing how to implement a simple animation.

Use
* candas.create*() to create an item,
* canvas.move() to move it,
* canvas.delete() to remove (and eventually redraw) it,
* canvas.after() to schedule an action by adding a callback.

See also http://tcl.tk/man/tcl8.7/TkCmd/canvas.html or https://web.archive.org/web/20200712234613/http://effbot.org/tkinterbook/canvas.htm.
"""
from tkinter import Tk, Canvas

UPDATE_EVERY_MS = 50
STEPSIZE = 1


class Ball:
    def __init__(self, canvas, y=0, radius=10, fill="red"):
        self.canvas = canvas
        self.x = 0
        self.y = y
        self.radius = radius
        self.fill = fill

        self.draw_ball()

    def draw_ball(self):
        self.ball = self.canvas.create_oval(
            *self._compute_oval_coordinates(), fill=self.fill
        )

    def _compute_oval_coordinates(self):
        x1 = self.x - self.radius
        x2 = self.x + self.radius
        y1 = self.y - self.radius
        y2 = self.y + self.radius

        return (x1, y1, x2, y2)

    def move_on_canvas(self):
        dx = STEPSIZE
        dy = 0
        self.canvas.move(self.ball, dx, dy)
        self.canvas.after(UPDATE_EVERY_MS, self.move_on_canvas)

    def redraw_on_canvas(self):
        self._move()
        self.canvas.delete(self.ball)
        self.draw_ball()
        self.canvas.after(UPDATE_EVERY_MS, self.redraw_on_canvas)

    def _move(self):
        self.x += STEPSIZE
        self.y += 0


if __name__ == "__main__":
    root = Tk()
    root.title("Moving Balls")
    root.resizable(False, False)
    canvas = Canvas(root, width=200, height=80)
    canvas.pack()

    moving_ball_1 = Ball(canvas, 10, fill="red")
    redrawing_ball_1 = Ball(canvas, 30, fill="yellow")
    moving_ball_2 = Ball(canvas, 50, fill="blue")
    redrawing_ball_2 = Ball(canvas, 70, fill="cyan")

    moving_ball_1.move_on_canvas()
    redrawing_ball_1.redraw_on_canvas()
    moving_ball_2.move_on_canvas()
    redrawing_ball_2.redraw_on_canvas()

    root.mainloop()
