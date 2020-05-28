from PIL import Image

class animal(object):
    pass


class Cat(animal):
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__color = "white"

    def getlegs(self) :
        return self.__legs

    def setlegs(self, l) :
        self.__legs = l

    def geteyes(self) :
        return self.__eyes

    def set_eyes(self, eyes):
        self.__eyes = eyes

    def get_color(self):
        return self.__color

    def set_color(sefl, color):
        self.__color = color



class Horse(animal):
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__color = "White"

   def getlegs(self):
       return self.__legs

   def setlegs(self, leg):
        self.__legs = l

   def geteyes(self):
       return self.__eyes

   def set_eyes(self, eyes):
       self.__eyes = eyes

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Dog(animal):
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__color = "Brown"

    def getlegs(self):
       return self.__legs

    def setlegs(self, l):
       return self.__legs = int(l)

    def geteyes(self):
        return self.__eyes

    def set_eyes(self, eyes):
        self.__eyes = int(eyes)

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = str(color)


class Elephant(animal):
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__color = 'Gray'
        self.__trunk = 1

    def get_legs(self):
        return self.__legs

    def get_eyes(self):
        return self.__eyes

    def get_trunk(self):
        return self.__trunk

    def get_color(self):
        return self.__color

    def set_legs(self, legs):
        self.__legs = legs

    def set_eyes(self, eyes):
        self.__eyes = eyes

    def set_trunk(self, trunk):
        self.__trunk = trunk

    def set_color(self, color):
        sefl.__color = color


class Tiger(animal):
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__color = 'Orange with black strips'

    def get_legs(self):
        return self.__legs

    def get_eyes(self):
        return self.__eyes

    def get_color(self):
        return self.__color

    def set_legs(self, legs):
        self.__legs = int(legs)

    def set_eyes(self, eyes):
        self.__eyes = int(eyes)

    def set_color(self, color):
        self.__color = str(color)


class Lion(animal):
    def __init__(self):
        self.__color = 'Orange'
        self.__legs = 4
        self.__eyes = 2

    def get_eyes(self):
        return self.__eyes

    def get_legs(self):
        return self.__legs

    def get_color(self):
        return self.__color

    def set_eyes(self, eyes):
        self.__eyes = int(eyes)

    def set_legs(self, legs):
        self.__legs = int(legs)

    def set_color(self, color):
        self.__color = str(color)

   
class Cow(animal):
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__color = 'White'

    def get_legs(self):
        return self.__legs

    def get_eyes(self):
        return self.__eyes

    def get_color(self):
        return self.__color

    def set_legs(self, legs):
        self.__legs = int(legs)

    def set_eyes(self, eyes):
        self.__eyes = int(eyes)

    def set_color(self, color):
        self.__color = color


class Ox(animal):
    def __init__(self):
        self.__color = 'White'
        self.__legs = 4
        self.__eyes = 2
        self.__ears = 2

    def get_eyes(self):
        return self.__eyes

    def get_legs(self): 
        return self.__legs
        
    def get_ears(self):
        return self.__ears

    def get_color(self):
        return self.__color

    def set_eyes(self, eyes):
        self.__eyes = int(eyes)

    def set_legs(self, legs):
        self.__legs = int(legs)

    def set_ears(self, ears):
        self.__ears = int(ears)

    def set_color(self, color):
        self.__color = str(color)



class Rabbit(animal):
    def __init__(self):
        self.__color = 'White'
        self.__legs = 4
        self.__eyes = 2
        self.__ears = 2

    def get_legs(self):
        return self.__legs

    def get_eyes(self):
        return self.__eyes

    def get_ears(self):
        return self.__ears

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = str(color)

    def set_legs(self, legs):
        self.__legs = legs

    def set_eyes(self, eyes):
        self.__eyes = int(eyes)

    def set_ears(self, ears):
        self.__ears = int(ears)

    def set_color(self, color):
        self.__color = str(color)


class Fox(animal):
    def __init__(self):
        self.__eyes = 2
        self.__ears = 2
        self.__legs = 4
        self.__color = 'Orange'

    def get_legs(self):
        return self.__eyes

    def get_ears(self):
        return self.__ears

    def get_eyes(self):
        return self.__eyes

    def get_color(self, color):
        return self.__color

    def set_legs(self, legs):
        self.__legs = int(legs)

    def set_ears(self, ears):
        self.__ears = int(ears)

    def set_eyes(self, eyes):
        self.__eyes = int(eyes)

    def set_color(self, color):
        self.__color = str(color)




