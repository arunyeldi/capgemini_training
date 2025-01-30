# print("Hello World")

# first_name = "Arun"
# last_name = "Yeldi"
# first_name = input("What is your first name: ")
# last_name = input("What is your last name: ")
# address = input("Please enter the address: ")
# pincode = input("Please enter the pincode: ")
# print(f"Hello {first_name} {last_name}, how are you?")
# print("I'm Good Arun")
# print(f"{address} is a beautiful place to visit")
# print(pincode)

# num_1 = int(input("Enter the number 1: "))
# num_2 = int(input("Enter the number 2: "))
# print(f"Summation of {num_1} and {num_2} is: {num_1 + num_2}")

# n = int(input("Enter a number: "));
# print(n / 10 * 10, n // 10 * 10)

# import random
# num = random.randint(1, 100)
# print(num)

import math
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
root_1 = int((-b + math.sqrt(b*b - 4 * a * c)) / (2 * a))
root_2 = int((-b - math.sqrt(b*b - 4 * a * c)) / (2 * a))
print(root_1)
print(root_2)