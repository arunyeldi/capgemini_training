class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"This car is: {self.brand} {self.model}")
car_obj = car("Lamborghini", "Huracan")
# car_obj.display()

class Employee:
    def __init__(self, name, salary, allowance, deduct_percent):
        self.__name = name
        self.__salary = salary
        self.__allowance = allowance
        self.__deduct_percent = deduct_percent

    def set_salary(self, salary):
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def salary_after_deduction(self):
        self.__salary = self.__salary - self.__salary * self.__deduct_percent
    
    def salary_after_allowance(self):
        self.__salary = self.__salary + self.__allowance

    
# emp = Employee("Alice", int(input("Enter the employee salary: ")), int(input("Enter the allowance: ")), 0.2)
# emp.salary_after_allowance()
# print("Salary after allowance: ", emp.get_salary())
# emp.salary_after_deduction()
# print("Salary after deduction: ", emp.get_salary())

# single inheritance

class Parent:
    def __init__(self):
        self.bignose = "6CM"

    def display_parent(self):
        print("This is the parent class.")

class Child(Parent):
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        super().__init__()
        print(f"This car is {self.model} {self.brand}")
    def display_child(self):
        print("This is the child class.")

# ch = Child("a", "b")
# ch.display_child()  
# ch.display_parent()
# print(ch.bignose)

class Student():
    



