class Employee:
    def __init__(self, name, id, department):
        self.name = name  
        self.id = id
        self.department = department
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.id}")
        print(f"Employee Department: {self.department}")

name = input("Enter Employee Name: ")
id = int(input("Enter Employee ID: "))
department = input("Enter Employee Department: ")
employee = Employee(name, id, department)
employee.display()