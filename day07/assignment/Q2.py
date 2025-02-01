from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    @abstractmethod
    def max_speed(self):
        pass
class Car(Vehicle):
    def max_speed(self):
        return "200 km/h"
class Bike(Vehicle):
    def max_speed(self):
        return "150 km/h"
vehicle_car = Car("Fortuner")
vehicle_bike = Bike("ZX900")
car_speed = vehicle_car.max_speed()
bike_speed = vehicle_bike.max_speed()
print(f"The car {vehicle_car.brand} is : {car_speed}")
print(f"The car {vehicle_bike.brand} is : {bike_speed}")