from graphics import *
from random import randrange

win = GraphWin("Simon", 900, 700, autoflush=False)
win.setBackground(color_rgb(0, 0, 0))

shape0 = Rectangle(Point(150 , 100), Point(350 , 300))
shape0.setOutline("black")
shape0.setFill(color_rgb(180, 0, 0))
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

def blackout():

    shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
    shape00.setFill(color_rgb(0, 0, 0))
    shape00.draw(win)


def ui():

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



def inside(point, rectangle):

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    greaterP1 = ll.getX() < point.getX() and ll.getY() < point.getY()
    greaterP2 = point.getX() < ur.getX() and point.getY() < ur.getY()

    result = greaterP1 and greaterP2

    return result

def System():

    rounds = 1

    points = 0

    coption = []

    Game = True

    while Game:

        coption = Pattern(rounds)

        for i in coption:
            blackout()

            update(3)

            if i == 1:
                update(3)
                shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                shape00.setOutline("black")
                shape00.setFill(color_rgb(180, 0, 0))
                shape00.setWidth(1)
                shape00.draw(win)
                update(3)

            elif i == 2:
                update(3)
                shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                shape00.setOutline("black")
                shape00.setFill(color_rgb(0, 0, 180))
                shape00.setWidth(1)
                shape00.draw(win)
                update(3)

            elif i == 3:
                update(3)
                shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                shape00.setOutline("black")
                shape00.setFill(color_rgb(0, 180, 0))
                shape00.setWidth(1)
                shape00.draw(win)
                update(3)


            elif i == 4:
                update(3)
                shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                shape00.setOutline("black")
                shape00.setFill(color_rgb(180, 180, 0))
                shape00.setWidth(1)
                shape00.draw(win)
                update(3)

            update(3)
            blackout()

        for i in coption:

            clickPoint = win.getMouse()

            user = answer(clickPoint)

            if not (user == i):
                Game = False
                break
            
        rounds += 1
        points += 1


def answer(click):

    global shape0, shape1, shape2, shape3

    if inside(click, shape0):
        return 1
    elif inside(click, shape1):
        return 2
    elif inside(click, shape2):
        return 3
    elif inside(click, shape3):
        return 4
    else:
        return 0

def Pattern(rounds):

    Colors = []

    for i in range(rounds):

        temp = randrange(1, 4)

        Colors.append(temp)

    return Colors



def main():

    ui()
    System()

    win.close()

main()