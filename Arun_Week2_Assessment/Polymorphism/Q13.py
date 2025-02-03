class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of square is: {self.side ** 2}")
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base 
        self.height = height

    def area(self):
        print(f"Area of triangle is: {(1 / 2) * self.base * self.height}")
    
square_obj = Square(int(input("Enter the side of a square: ")))
square_obj.area()

triangle_obj = Triangle(int(input("Enter the base value of triangle: ")), int(input("Enter the height of a triangle: ")))
triangle_obj.area()
