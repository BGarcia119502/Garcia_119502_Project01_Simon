from graphics import *
from random import randrange

class Graphics():

    def __init__(self, window):
        self.window = window
        win = GraphWin("Simon", 900, 700, autoflush=False)
        win.setBackground(color_rgb(0, 0, 0))
        o = Oval(Point(350, 300), Point(550, 400))
        o.setOutline(color_rgb(75, 75, 75))
        o.setFill(color_rgb(55, 55, 55))
        o.setWidth(2)
        o.draw(window)

        t = Text(Point(450, 350), "Simon")
        t.setFill("white")
        t.setFace("helvetica")
        t.setSize(24)
        t.setStyle("bold")
        t.draw(window)

    def GUI1(self, window):
        shape0 = Rectangle(Point(150 , 100), Point(350 , 300))
        shape0.setOutline("black")
        shape0.setFill(color_rgb(180, 0, 0))
        shape0.setWidth(1)
        shape0.draw(window)
    
    def GUI2(self, window):
        shape1 = Rectangle(Point(150 , 400), Point(350 , 600))
        shape1.setOutline("black")
        shape1.setFill(color_rgb(0, 0, 180))
        shape1.setWidth(1)
        shape1.draw(window)

    def GUI3(self, window):
        shape2 = Rectangle(Point(550 , 100), Point(750 , 300))
        shape2.setOutline("black")
        shape2.setFill(color_rgb(0, 180, 0))
        shape2.setWidth(1)
        shape2.draw(window)
    def GUI4(self, window):
        shape3 = Rectangle(Point(550 , 400), Point(750 , 600))
        shape3.setOutline("black")
        shape3.setFill(color_rgb(180, 180, 0))
        shape3.setWidth(1)
        shape3.draw(window)


class Game(Graphics):

    def __init__(self, rectangle, window):

        self.window = window

        self.ll = rectangle.getP1()  # assume p1 is ll (lower left)
        self.ur = rectangle.getP2()  # assume p2 is ur (upper right)

        

    def inside(self, point):

        greaterP1 = self.ll.getX() < point.getX() and self.ll.getY() < point.getY()
        greaterP2 = point.getX() < self.ur.getX() and point.getY() < self.ur.getY()

        result = greaterP1 and greaterP2

        return result

    def System(self):

        rounds = 1

        points = 0

        coption = []

        Game = True

        while Game:

            coption = self.Pattern(rounds)

            for i in coption:
                self.blackout()

                update(3)

                if i == 1: #Red
                    update(3)
                    shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                    shape00.setOutline("black")
                    shape00.setFill(color_rgb(180, 0, 0))
                    shape00.setWidth(1)
                    shape00.draw(self.window)
                    update(3)

                elif i == 2: #Blue
                    update(3)
                    shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                    shape00.setOutline("black")
                    shape00.setFill(color_rgb(0, 0, 180))
                    shape00.setWidth(1)
                    shape00.draw(self.window)
                    update(3)

                elif i == 3: #Green
                    update(3)
                    shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                    shape00.setOutline("black")
                    shape00.setFill(color_rgb(0, 180, 0))
                    shape00.setWidth(1)
                    shape00.draw(self.window)
                    update(3)


                elif i == 4: #Yellow
                    update(3)
                    shape00 =  Rectangle(Point(430 , 50), Point(470 , 90))
                    shape00.setOutline("black")
                    shape00.setFill(color_rgb(180, 180, 0))
                    shape00.setWidth(1)
                    shape00.draw(self.window)
                    update(3)

                update(3)
                self.blackout()

        for i in coption:

            clickPoint = self.window.getMouse()

            user = self.answer(clickPoint)

            if not (user == i):
                Game = False
                break
            
        rounds += 1
        points += 1

    def answer(self):

        GUI = Graphics()

        if self.inside(GUI.GUI1()):
            return 1
        elif self.inside(GUI.GUI2()):
            return 2
        elif self.inside(GUI.GUI3()):
            return 3
        elif self.inside(GUI.GUI4()):
            return 4
        else:
            return 0

    def Pattern(self, rounds):

        Colors = []

        for i in range(rounds):

            temp = randrange(1, 4)

            Colors.append(temp)

        return Colors



def main():

    G = Graphics()
    Start = Game()

main()