from graphics import *
from math import sqrt
from time import sleep
win = GraphWin("elipse", 400, 400)
win.setCoords(-4.0,-4.0,4.0,4.0)
l1 = Line(Point(0,-4), Point(0,4))
l1.draw(win)
l2 = Line(Point(4,0), Point(-4,0))
l2.draw(win)
l2.draw
# x**2 + 2 * y**2 = 4
# 2 * y**2 = 4 - x**2
# y**2 = (4 - x**2) / 2
# y = sqrt((4 - x**2) / 2)

increment = .2
x = -2.0
while x <= 2.0:
    v = (4 - x**2) / 2
    y = sqrt(v)
    Circle(Point(x, y), .05).draw(win)
    print(x, y)
    x = x + increment
x = 2
while x >= -2.0:
    v = (4 - x**2) / 2
    y = sqrt(v)
    Circle(Point(x, -y), .05).draw(win)
    print(x, y)
    x = x - increment

c = Circle(Point(2,2), .05)
c.draw(win)
sleep(1)
c.move(-1,-1)
