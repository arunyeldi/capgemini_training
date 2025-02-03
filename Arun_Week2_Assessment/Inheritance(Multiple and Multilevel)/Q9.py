class Car:
    def move(self):
        print("Car moves on the land")
    
class Airplane:
    def move(self):
        print("Airplane moves in the air")

class FlyingCar(Car, Airplane):
    def move(self):
        Car.move(self)
        Airplane.move(self)
        print("This is a FlyingCar")

# car_obj = Car()
# car_obj.move()

# airplane_obj = Airplane()
# airplane_obj.move()

flying_car_obj = FlyingCar()
flying_car_obj.move()