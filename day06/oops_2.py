class Animal():
    color = "black"
    def sound(s):
        print("Barks")
        # print(s)
# obj = Animal()
# print(obj.color)
# obj.sound()
# print(obj)

# polymorphism examples
class Add:
    def add(s, a, b, c = 0):
        print(a + b + c)
obj = Add()
# obj.add(2, 5)
# obj.add(1, 8, 5)

# list of parameters 
class Example:
    def __init__(s, name):
        print(f"First Constructor: Hello {name}")
    
    def __init__(s, age):
        print(f"Second Constructor: Age is {age}")

# obj = Example(21)

class Example:
    def __init__(s, studentName, **k):
        s.k = k
        if 'name' in k and 'age' in k:
            print(k['name'], studentName, k['age'])
        elif 'name' in k:
            print(k['name'], studentName)
    def display(s):
        for key, value in s.k.items():
            print(f"Key : 
            {key}, Value : {value}")

obj_1 = Example("kOHLI", name = "Virat")
obj_2 = Example("kOHLI", name = "Virat", age = 26)
obj_1.display()
