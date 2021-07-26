from graphics import *
from math import sqrt
from time import sleep

# Math for elipse
# x**2 + 2 * y**2 = 4
# 2 * y**2 = 4 - x**2
# y**2 = (4 - x**2) / 2
# y = sqrt((4 - x**2) / 2)
# center is (h,k), which is (0,0) for this elipse
# foci are (h+c,k) and (h-c,k), or (c,0) and (-c,0)
# c**2 = a**2 - b**2, a is major axis, b is minor axis
# c = sqrt(a**2 - b**2)
# c = sqrt(2**2 - 1**2)
# c = sqrt(3), which is 1.732
# I use 1.4 as c. The sun looks better there

def draw_grid(win):
    l1 = Line(Point(0,-4), Point(0,4))
    l1.draw(win)
    l2 = Line(Point(4,0), Point(-4,0))
    l2.draw(win)
    l2.draw

def draw_elipse(win, increment, sleep_val):
    global earth_color

    def mouse_checker():
        global earth_color
        m = win.checkMouse()
        if m:
            dx = m.getX() - c.getCenter().getX()
            dy = m.getY() - c.getCenter().getY()
            if sqrt(dx**2 + dy**2) < .5:
                if earth_color == 'blue':
                    earth_color = 'red'
                else:
                    earth_color = 'blue'

    x = -2.0
    c = 0
    while x <= 2.0:
        y = sqrt((4 - x**2) / 2)
        if c:
            c.undraw()
        c = Circle(Point(x, y), .05)
        c.setFill(earth_color)
        c.draw(win)
        mouse_checker()
        sleep(sleep_val)
        x = x + increment
        if x >= 2:
            increment = -increment
    x = 2
    while x >= -2.0:
        y = sqrt((4 - x**2) / 2)
        if c:
            c.undraw()
        c = Circle(Point(x, -y), .05)
        c.setFill(earth_color)
        c.draw(win)
        mouse_checker()
        sleep(sleep_val)
        x = x - increment
    c.undraw()

def orbits(win, increment, sleep_val, n):
    for i in range(n):
        draw_elipse(win, increment, sleep_val)

def main():
    win = GraphWin("elipse", 400, 400)
    win.setCoords(-4.0,-4.0,4.0,4.0)
    draw_grid(win)
    sun = Circle(Point(1.4, 0), .3)
    sun.setFill("yellow")
    sun.draw(win)
    orbits(win, .05, .05, 3)
    #draw_elipse(win, .1, .1)
    c = Circle(Point(2,2), .05)
    c.draw(win)
    sleep(1)
    c.move(-1,-1)

earth_color = 'blue' # global has earth's color

main()
