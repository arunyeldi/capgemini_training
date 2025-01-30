class Animal():
    color = "blackwargs"
    def sound(self):
        print("Barkwargss")
        # print(self)
# obj = Animal()
# print(obj.color)
# obj.sound()
# print(obj)

# polymorphism examples
class Add:
    def add(self, a, b, c = 0):
        print(a + b + c)
obj = Add()
# obj.add(2, 5)
# obj.add(1, 8, 5)

# list of parameters 
class Example:
    def __init__(self, name):
        print(f"First Constructor: Hello {name}")
    
    def __init__(self, age):
        print(f"Second Constructor: Age is {age}")

# obj = Example(21)

class Example:
    def __init__(self, studentName, **kwargs):
        self.kwargs = kwargs
        if 'name' in kwargs and 'age' in kwargs:
            print(kwargs['name'], studentName, kwargs['age'])
        elif 'name' in kwargs:
            print(kwargs['name'], studentName)
    def display(self):
        for key, value in self.kwargs.items():
            print(f"key : {key}, Value : {value}")

# obj_1 = Example("KOHLI", name = "Virat")
# obj_2 = Example("KOHLI", name = "Virat", age = 26)
# obj_1.display()


# multiple inheritance
class Lion:
    def roar(self):
        return 'Lion can roar.'

class Dog:
    def bark(self):
        return 'Dog can bark'

class Animal(Lion, Dog):
    def __init__(self, eat):
        self.eat = eat
    def make_sound(self):
        print("Animal can make sound")

obj = Animal("Non-Veg")
# print(obj.roar())
# print(obj.bark())
# print(f"Animal eat: {obj.eat}")
# obj.make_sound()



# Multi level iniheritance
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
obj_1 = Circle(5)
print(f"Area of circle is: {obj_1.area()}")

obj_2 = Rectangle(2, 5)
print(f"Area of rectangle is: {obj_2.area()}")
    
