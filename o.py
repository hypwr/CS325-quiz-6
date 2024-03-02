from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = (math.pi)*(self.radius**2) 
        return area

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def get_area(self):
        area = (self.length)*(self.width)
        return area

class Square(Shape):
    def __init__(self,length):
        self.side_length = length

    def get_area(self):
        area = (self.side_length)**2
        return area

def main():
    circle = Circle(5)
    rectangle = Rectangle(5,10)
    square = Square(5)
    print("Circle Area: "+str(circle.get_area()))
    print("Rectangle Area: "+str(rectangle.get_area()))
    print("Square Area: "+str(square.get_area()))

main()