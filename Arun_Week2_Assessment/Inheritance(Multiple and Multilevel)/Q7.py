class Person:
    def display_details(self):
        print("This is person class")

class Employee(Person):
    def display_details(self):
        super().display_details()
        print("This is employee class")

class Manager(Employee):
    def display_details(self):
        super().display_details()
        print("This is manager class")

    def approve_leave(self, is_approve_leave):
        if is_approve_leave == 'yes':
            print("Is approve leave: Yes")
        else:
            print("Is approve leave: No")
        

person_obj = Person()
person_obj.display_details()

employee_obj = Employee()
employee_obj.display_details()

manager_obj = Manager()
manager_obj.display_details()
manager_obj.approve_leave('yes')


