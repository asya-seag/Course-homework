import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Triangle perimeter:", perim)
        return perim


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print("Rectangle perimeter:", perim)
        return perim


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def calc_perimeter(self):
        perim = 4 * self.a
        print("Square perimeter:", perim)
        return perim

# triangle = Triangle(2, 4, 5)
# triangle.calc_perimeter()

rectangle = Rectangle(3, 4)
rectangle.calc_perimeter()

square = Square(3)
square.calc_perimeter()