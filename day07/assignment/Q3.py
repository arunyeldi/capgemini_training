from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self, length, width):
        return length * width
class Circle(Shape):
    def area(self, radius):
        return 3.14 * (radius ** 2)

rectangle = Rectangle()
area_of_rectangle = rectangle.area(int(input("Enter the length: ")), int(input("Enter the width: ")))
print(f"The area of rectangle is: {area_of_rectangle}")
circle = Circle()
area_of_circle = circle.area(int(input("Enter the radius of a circle: ")))
print(f"The area of circle is: {area_of_circle}")