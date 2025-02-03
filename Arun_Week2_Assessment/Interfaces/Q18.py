from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass

class BasicCalculator(ICalculator):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 - self.number2
    def multiply(self):
        return self.number1 * self.number2
    def divide(self):
        return self.number1 / self.number2 if self.number2 != 0 else "Cannot divide by zero"
    
i_cal_obj = BasicCalculator(int(input("Enter number 1: ")), int(input("Enter number 2: ")))
print(f"Addition: {i_cal_obj.add()}")
print(f"Subtraction: {i_cal_obj.subtract()}")
print(f"Multiplication: {i_cal_obj.multiply()}")
print(f"Division: {i_cal_obj.divide()}")
