# -*- coding: latin-1 -*-
"""
Snippet showing how to implement a simple animation.

Use
* candas.create*() to create an item,
* canvas.move() to move it,
* canvas.delete() to remove (and eventually redraw) it,
* canvas.after() to schedule an action by adding a callback.

See also
* http://tcl.tk/man/tcl8.7/TkCmd/canvas.html
* or https://web.archive.org/web/20200712234613/http://effbot.org/tkinterbook/canvas.htm.
* https://stackoverflow.com/questions/42418190/exit-a-tkinter-window-after-a-certain-time-period
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
    radius = 10
    n_balls = 10
    height = 2 * radius * 2 * n_balls
    color_move = "red"
    color_redraw = "blue"

    root = Tk()
    root.title("Animation (move={!r}, redraw={!r})".format(color_move, color_redraw))
    root.resizable(False, False)
    root.after(5000, root.destroy)

    canvas = Canvas(root, width=600, height=height)
    canvas.pack()

    y0 = radius
    for i in range(n_balls):
        yi = y0 + i * 2 * radius
        ball = Ball(canvas, y=yi, fill=color_move)
        ball.move_on_canvas()

    y0 = yi + 2 * radius
    for i in range(n_balls):
        yi = y0 + i * 2 * radius
        ball = Ball(canvas, y=yi, fill=color_redraw)
        ball.redraw_on_canvas()

    root.mainloop()
