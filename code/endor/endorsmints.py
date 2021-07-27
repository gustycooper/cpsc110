#endor.py

from graphics import *
import calduum

class Button:
    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        return(self.active and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def setLabel(self, label):
        self.label.setText(label)

    def setLabelColor(self, c):
        self.label.setTextColor(c)

    def setFill(self, c):
        self.rect.setFill(c)

    def activate(self):
        #self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
    
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

class Endor:
    def __init__(self, name, val1s, val2s):
        self.win = GraphWin(name, 400, 600)
        #win.setCoords(0.0,0.0,4.0,4.0)
        self.buysellEntry = Entry(Point(100, 15), 20)
        self.buysellEntry.setTextColor("white")
        self.buysellEntry.draw(self.win)
        self.buysellText = Text(Point(100, 35), "Acres to Sell")
        self.buysellText.draw(self.win)
        self.buysellButton = Button(self.win, Point(220,25), 40, 40, "Sell")
        self.buysellButton.setFill("Blue")
        self.buysellButton.setLabel("Sell")
        self.buysellButton.setLabelColor("white")
        self.buysellButton.activate()
        self.buysellColor = "Blue"
        self.enterButton = Button(self.win, Point(220,110), 40, 40, "Enter")
        self.enterButton.setLabelColor("red")
        self.enterButton.activate()
        self.feedEntry = Entry(Point(100, 65), 20)
        self.feedEntry.setTextColor("white")
        self.feedEntry.draw(self.win)
        self.feedText = Text(Point(100, 85), "Bushels to Feed")
        self.feedText.draw(self.win)
        self.plantEntry = Entry(Point(100, 115), 20)
        self.plantEntry.setTextColor("white")
        self.plantEntry.draw(self.win)
        self.plantText = Text(Point(100,135),"Acres to plant")
        self.plantText.draw(self.win)
        self.outborder = Rectangle(Point(10, 180), Point(390, 450))
        self.outborder.draw(self.win)
        self.errorText = Text(Point(200, 170), "")
        self.errorText.setTextColor("red")
        self.errorText.draw(self.win)
        
        self.debugText = Text(Point(200,575),"") # 100 is center, 160 is down
        self.debugText.draw(self.win)
        self.outText = []
        x = 200
        y = 190
        for val1, val2 in zip(val1s,val2s):
            t = Text(Point(x,y), val1 + str(val2))
            t.draw(self.win)
            self.outText.append(t)
            y = y + 15

    # val1s - list of strings
    # val2s - list of ints
    # val1s and val2s are equal lenght
    def displayResults(self, val1s, val2s):
        for txt, val1, val2 in zip(self.outText,val1s,val2s):
            txt.undraw()
            txt.setText(val1 + str(val2))
            txt.draw(self.win)

    def eventLoop(self):
        keepLooping = True
        while keepLooping:
            p = self.win.getMouse()
            if self.enterButton.clicked(p):
                goodvals = True
                buysellbuttonval = self.buysellButton.getLabel()
                a2buysell = self.buysellEntry.getText()
                b2feed = self.feedEntry.getText()
                a2plant = self.plantEntry.getText()
                userInput = a2buysell + " " + b2feed + " " + a2plant
                self.debugText.setText(userInput + " " + self.buysellColor + " " + buysellbuttonval)
                self.debugText.setFill(self.buysellColor)
                if not a2buysell.isnumeric():
                    self.buysellEntry.setText("Must be number")
                    goodvals = False
                elif buysellbuttonval == "Buy":
                    a2buy = int(a2buysell)
                    a2sell = 0
                else:
                    a2buy = 0
                    a2sell = int(a2buysell)
                if not b2feed.isnumeric():
                    self.feedEntry.setText("Must be number")
                    goodvals = False
                else:
                    b2feed = int(b2feed)
                if not a2plant.isnumeric():
                    self.plantEntry.setText("Must be number")
                    goodvals = False
                else:
                    a2plant = int(a2plant)
                if goodvals:
                    ok, out_lines, out_ints = calduum.simulateYear(a2buy, a2sell, b2feed, a2plant)
                    if ok:
                        self.errorText.setText("")
                        self.displayResults(out_lines, out_ints)
                    else:
                        self.errorText.setText(out_lines + " " + out_ints)
            elif self.buysellButton.clicked(p):
                if self.buysellColor == "Blue":
                    self.buysellButton.setFill("Red")
                    self.buysellColor = "Red"
                    self.buysellButton.setLabel("Buy")
                    self.buysellButton.setLabelColor("yellow")
                    self.buysellText.setText("Acres to Buy")

                else:
                    self.buysellButton.setFill("Blue")
                    self.buysellColor = "Blue"
                    self.buysellButton.setLabel("Sell")
                    self.buysellButton.setLabelColor("white")
                    self.buysellText.setText("Acres to Sell")
            else:
                self.debugText.setText("Click anywhere to close")
                self.win.getMouse()
                self.win.close()
                keepLooping = False

