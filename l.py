import math

class Shape:
    def get_area(self):
        raise NotImplementedError("Subclass must impliment get_area")

class HasWidth:
    def set_width(self):
        raise NotImplementedError("Subclass must implement set_width()")
    
class HasLength:
    def set_length(self):
        raise NotImplementedError("Subclass must implement set_length()")

class HasHeight:
    def set_height(self):
        raise NotImplementedError("Subclass must implement set_height()")
    
class HasSides:
    def set_sides(self):
        raise NotImplementedError("Subclass must implement set_sides()")

class Circle(Shape, HasWidth, HasHeight):
    def __init__(self):
        self.height = 0
        self.width = 0

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        area = (math.pi)*((self.height/2)*(self.width/2)) 
        return area

class Rectangle(Shape, HasWidth, HasHeight):
    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        area = (self.height)*(self.width)
        return area

class Triangle(Shape, HasLength):
    def set_length(self,length):
        self.length = length

    def get_area(self):
        area = (self.length**2)/2
        return area
    
class Polygon(Shape, HasSides, HasLength):
    def set_sides(self, sides):
        self.sides = sides

    def set_length(self, length):
        self.length = length

    def get_area(self):
        area = ((self.sides)*(self.length))*((self.length/(2*math.tan(math.pi/self.sides))))/2
        return area
    
def main():
    circle=Circle()
    rectangle=Rectangle()
    triangle=Triangle()
    polygon5=Polygon()

    circle.set_height(10)
    circle.set_width(20)
    print("Circle: "+str(circle.get_area()))

    rectangle.set_height(10)
    rectangle.set_width(20)
    print("Rectangle: "+str(rectangle.get_area()))

    triangle.set_length(5)
    print("Triangle: "+str(triangle.get_area()))

    polygon5.set_length(15)
    polygon5.set_sides(5)
    print("5 Sided Polygon: "+str(polygon5.get_area()))

main()

#might need to redo this one