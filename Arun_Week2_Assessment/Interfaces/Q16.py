from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
    
rectangle_obj = Rectangle(int(input("Enter the length: ")), int(input("Enter the width: ")))
print(f"Area of rectangle is: {rectangle_obj.calculate_area()}")

circle_obj = Circle(int(input("Enter the radius of a circle: ")))
print(f"Area of circle is: {circle_obj.calculate_area()}")