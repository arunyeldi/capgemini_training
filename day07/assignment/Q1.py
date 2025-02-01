from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()