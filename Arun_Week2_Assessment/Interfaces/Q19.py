from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class Car(IVehicle):
    def start_engine(self):
        print("Car Engine has started")
    def stop_engine(self):
        print("Car Engine has stopped")

class Bike(IVehicle):
    def start_engine(self):
        print("Bike Engine has started")
    def stop_engine(self):
        print("Bike Engine has stopped")
    
class Truck(IVehicle):
    def start_engine(self):
        print("Truck Engine has started")
    def stop_engine(self):
        print("Truck Engine has stopped")

car_obj = Car()
car_obj.start_engine()
car_obj.stop_engine()

bike_obj = Bike()
bike_obj.start_engine()
bike_obj.stop_engine()

truck_obj = Truck()
truck_obj.start_engine()
truck_obj.stop_engine()