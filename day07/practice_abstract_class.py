from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        print("Concrete method")

class Son(Father):
    def display(self):
        print('Son is implementing in the abstract method')

class Daughter(Father):
    def display(self):
        print("Daughter is implementing in the abstract class")

son = Son()
daughter = Daughter()
son.display()
daughter.display()
