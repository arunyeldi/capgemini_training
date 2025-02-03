class Vehicle:
    def display(self):
        print("This is vehicle")
class Car(Vehicle):
    def display(self):
        super().display()
        print("This is car")
class Bike(Vehicle):
    def display(self):
        super().display()
        print("This is bike")
class Electric_car(Car):
    def display(self):
        super().display()
        print("This is electric car")

vehicle_obj = Vehicle()
vehicle_obj.display()

car_obj = Car()
car_obj.display()

bike_obj = Bike()
bike_obj.display()

electric_car_obj = Electric_car()
electric_car_obj.display()