from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        print("Successfully logged into Google")
    def logout(self):
        print("Successfully logged out from Google")

class FacebookAuth(UserAuthentication):
    def login(self):
        print("Successfully logged into Facebook")
    def logout(self):
        print("Successfully logged out from Facebook")

google_obj = GoogleAuth()
google_obj.login()
google_obj.logout()

facebook_obj = FacebookAuth()
facebook_obj.login()
facebook_obj.logout()