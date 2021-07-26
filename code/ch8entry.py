from graphics import *
XMIN = 80
XMAX = 120
YMIN = 70
YMAX = 110

def main():
    w = GraphWin("Entry Examples", 200, 150)
    t = Text(Point(40,20), "Name")
    t.draw(w)
    e = Entry(Point(100,20), 10)
    e.draw(w)
    b = Rectangle(Point(80,70), Point(120, 110))
    b.draw(w)
    bt = Text(Point(100, 90), "Enter")
    bt.draw(w)
    ot = Text(Point(100, 50), "")
    ot.draw(w)

    while True:
        m = w.getMouse()
        if XMIN <= m.getX() <= XMAX and YMIN <= m.getY() <= YMAX:
            intxt = e.getText()
            if intxt == 'q' or intxt == 'Q':
                break
            ot.setText('You entered: ' + intxt)
            print('You entered:', intxt)
    
    w.close()

main()
