class Student:
    def __init__(self, name, roll_number):
        self.name = name 
        self.roll_number = roll_number
    
    def student_details(self):
        return self.name, self.roll_number
    
name = input("Enter your name: ")
roll_number = input("Enter your roll number: ")
student_obj = Student(name, roll_number)
name, roll_number = student_obj.student_details()
print(f"Your name is : {name} and \nYour roll number is : {roll_number}")