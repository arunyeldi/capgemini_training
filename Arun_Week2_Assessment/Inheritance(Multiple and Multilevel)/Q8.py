class Animal:
    def speak(self):
        print("This is Animal class")

class Dog(Animal):
    def speak(self):
        print("Bark")
    
class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog()
dog.speak()

cat  = Cat()
cat.speak()