import math
import turtle
import random

class circle :
    def __init__(self, r = 1) :
        self.__radius = r
        
    def getarea(self) :
        area = self.__radius * self.__radius * math.pi
        return print("The area of circle is {0:.2f} sq.units. " .format(area))

    def getcircumference(self):
        a = math.pi * 2 * self.__radius
        return print("The circumference of the circle is {0:.2f} units.".format(a))

    def drawcircle(self):
        print("Drawing the circle ")
        turtle.circle(self.__radius)

    def drawradius(self) :
        self.drawcircle()
        print("Drawing the radius ")
        #turtle.circle(self.__radius)
        turtle.penup()
        turtle.goto(0, self.__radius)
        turtle.pendown()
        turtle.goto(self.__radius, self.__radius)
        turtle.penup()

    def drawdiameter(self):
        #turtle.circle(self.__radius)
        self.drawcircle()
        print("Drawing the diameter")
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(0, 2 * self.__radius)
        turtle.penup()


        
class triangle :
    def __init__(self, l=100, m = 100, n = 100) :
        self.__a = l
        self.__b = l
        self.__c = l

    def getperimeter(self):
        a = self.__a + self.__b + self.__c
        return print("The perimeter of triangle is {0: .2f} unit" .format(a))

    def getarea(self):
        s = self.__a + self.__b + self.__c
        s = s/2
        a = s - self.__a
        b = s - self.__b
        c = s - self.__c
        areasq = s * a * b * c
        area = math.sqrt(areasq)
        print("The area of the triangle is : {0: .2f} sq units".format(area))
    


class rectangle :
    def __init__(self, l = 100, b = 100):
        if l * b > 0:
            self.__l = l
            self.__b = b
        else:
            print("Give valid length and breadth of rectangle. ")
            return

    def getarea(self):
        area = self.__l * self.__b
        return print("The area of rectangle is {0: .2f} sq units".format(area))
    def getperimeter(self):
        p = 2 * (self.__l + self.__b)
        return print("The perimeter of the rectangle is {0: .2f} units.".format(p))
    
    def drawrectangle(self):
        r = random.randint(0, 100)
        print("The rectangle will be drawn : ")
        #print(r)
        if r % 2 == 0:
            turtle.pendown()
            turtle.goto(self.__l, 0)
            turtle.goto(self.__l,self.__b)
            turtle.goto(0, self.__b)
            turtle.goto(0, 0)
            turtle.penup()
        else:
            turtle.pendown()
            turtle.goto(self.__b, 0)
            turtle.goto(self.__b, self.__l)
            turtle.goto(0, self.__l)
            turtle.goto(0, 0)
            turtle.penup()

class square :
    def __init__(self, side = 100):
        
        self.side = side

    def getarea(self):
        area = self.side * self.side
        return area

    def getperimeter(self):
        perimeter = self.side * 4
        return perimeter
    
    def drawsquare(self):
        turtle.pendown()
        turtle.goto(self.side, 0)
        turtle.goto(self.side, self.side)
        turtle.goto(0, self.side)
        turtle.goto(0, 0)
        turtle.penup()



class elipse :
    def __init__(self, a = 100, b = 50):
        self.a = a
        self.b = b

    def getarea(self):
        area = self.a * self.b * math.pi
        return area

    def get_perimeter(self):
        a = (3 * self.a + b) * (self.a + 3 * self.b)
        a = math.sqrt(a)
        b = 3 * (self.a + self.b)
        a = b - a
        perimeter = math.pi * a
        return perimeter


class hexagon:
    def __init__(self, a = 100):
        self.a = a

    def getperimeter(self):
        perimeter = self.a * 6
        return perimeter

    def getarea(self):
        a = (self.a**2) * (math.sqrt(3))/2
        return a * 6


class pentagon :
    def __init__(self, a = 100):
        self.a = a

    def getperimeter(self):
        return self.a * 5

    def getarea(self):
        a = 5 + 2 * math.sqrt(5)
        a = a * 5
        area = math.sqrt(a)
        area = area * self.a * self.a/4
        print(area)
        return


class octagon :
    def __init__(self, side):
        self.side = side
    
    def get_perimeter(self):
        p = self.side * 8
        return p

    def get_area(self):
        a = 1 + math.sqrt(2)
        a = a * 2
        area = self.side * self.side * a
        return area


