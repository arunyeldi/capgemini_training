class Notification:
    def send(self):
        print("This is parent class")

class EmailNotification(Notification):
    def send(self):
        print("This is an Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("This is an SMS Notification")

emial_obj = EmailNotification()
emial_obj.send()

sms_obj = SMSNotification()
sms_obj.send()