from graphics import *
from random import *
def main():

    win = GraphWin("Simon", 900, 700)
    win.setBackground(color_rgb(10, 10, 10))

    o = Oval(Point(350, 300), Point(550, 400))
    o.setOutline(color_rgb(75, 75, 75))
    o.setFill(color_rgb(55, 55, 55))
    o.setWidth(2)
    o.draw(win)

    t = Text(Point(450, 350), "Simon")
    t.setFill("white")
    t.setFace("helvetica")
    t.setSize(24)
    t.setStyle("bold")
    t.draw(win)

    shape0 = Rectangle(Point(150 , 100), Point(350 , 300))
    shape0.setOutline("black")
    shape0.setFill(color_rgb(180, 5, 5))
    shape0.setWidth(1)
    shape0.draw(win)

    shape1 = Rectangle(Point(150 , 400), Point(350 , 600))
    shape1.setOutline("black")
    shape1.setFill(color_rgb(0, 0, 180))
    shape1.setWidth(1)
    shape1.draw(win)

    shape2 = Rectangle(Point(550 , 100), Point(750 , 300))
    shape2.setOutline("black")
    shape2.setFill(color_rgb(0, 180, 0))
    shape2.setWidth(1)
    shape2.draw(win)

    shape3 = Rectangle(Point(550 , 400), Point(750 , 600))
    shape3.setOutline("black")
    shape3.setFill(color_rgb(180, 180, 0))
    shape3.setWidth(1)
    shape3.draw(win)

    win.getMouse()
    win.close()

main()