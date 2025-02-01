from abc import ABC, abstractmethod
class Father:
    @abstractmethod
    def profession(self):
        pass
    def introduce(self):
        self.profession()
class Engineer(Father):
    def profession(self):
        print("I'm an Engineer")
class Doctor(Father):
    def profession(self):
        print("I'm a Doctor")


engineer = Engineer()
engineer.introduce()

doctor = Doctor()
doctor.introduce()