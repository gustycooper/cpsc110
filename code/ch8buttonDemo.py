# butFuncDemo.py
# This program demostrates how to use the libraries butFunc.py

from graphics import *
from button import *

def main():
    # GraphWin win
    # Button enterButton, toggleButton
    # Text output
    # Entry input
    # Point p
    # string toggleColor
    # Boolean keepLooping
    win = GraphWin("Button Demo", 400, 400)
    #win.setCoords(0.0,0.0,4.0,4.0)
    enterButton = Button(win, Point(220,110), 40, 40, "Enter")
    enterButton.activate()
    toggleButton = Button(win, Point(270,110), 40, 40, "Toggle")
    toggleButton.setFill("Blue")
    toggleButton.setLabel("Toggle")
    toggleButton.setLabelColor("white")
    toggleButton.activate()
    toggleColor = "Blue"
    entry = Entry(Point(100, 115), 20)
    entry.draw(win)
    output = Text(Point(100,135),"")
    output.draw(win)
    keepLooping = True
    while keepLooping:
        p = win.getMouse()
        if enterButton.clicked(p):
            userInput = entry.getText()
            toggleLabel = toggleButton.getLabel()
            output.setText(userInput + " " + toggleColor + " " + toggleLabel)
            output.setFill(toggleColor)
            print("Enter Button Clicked")
        elif toggleButton.clicked(p):
            if toggleColor == "Blue":
                toggleButton.setFill("Red")
                toggleColor = "Red"
                toggleButton.setLabel("Tiggle")
                toggleButton.setLabelColor("yellow")

            else:
                toggleButton.setFill("Blue")
                toggleColor = "Blue"
                toggleButton.setLabel("Toggle")
                toggleButton.setLabelColor("white")
        else:
            output.setText("Click anywhere to close")
            win.getMouse()
            win.close()
            keepLooping = False

main()
