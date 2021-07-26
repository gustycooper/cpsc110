from graphics import *
from button import *

def main():
    w = GraphWin("Entry Examples", 200, 150)
    t = Text(Point(40,20), "Name")
    t.draw(w)
    e = Entry(Point(100,20), 10)
    e.draw(w)
    b = Button(w, Point(100, 90), 40, 40, "Enter")
    b.activate()
    ot = Text(Point(100, 50), "")
    ot.draw(w)

    while True:
        m = w.getMouse()
        if b.clicked(m):
            intxt = e.getText()
            if intxt == 'q' or intxt == 'Q':
                break
            ot.setText('You entered: ' + intxt)
            print('You entered:', intxt)
    
    w.close()

main()
