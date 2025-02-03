class Electronics:
    def display_content(self):
        self.items = {'Book': 25}
        print("This is parent class")

class MobileDevice(Electronics):
    def display_content(self):
        super().display_content()
        print("This is mobile device class")

class SmartPhone(MobileDevice):
    def display_content(self):
        super().display_content()
        print(self.items)
        print("This is a smart phone class")

smart_phone_obj = SmartPhone()
smart_phone_obj.display_content()