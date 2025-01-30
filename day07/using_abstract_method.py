class Parent:
    def __init__(self):
        pass   
    def display(self):
        pass

class Child(Parent):   
    def display(self):
        print("Child is implementing in the abstract class")
    
child = Child()
child.display()