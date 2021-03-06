import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    """ Draws n line segments with the given length and angle (in degrees) between them.
    t is a turtle. """

    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


bob = turtle.Turtle()
arc(bob, 50, 360)

turtle.mainloop()
