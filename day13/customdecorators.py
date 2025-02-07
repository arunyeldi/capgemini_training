import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)
        print("Before the function call")
        result = func(*args, **kwargs)
        
        print("After the function call")
        time.sleep(1)
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
    

greet("Arun")
