# Program to calculate the factorial of a given number 

def get_input():
    user_input = input("Enter the number to calculate the factorial: ")
    return user_input

def calculate_factorial(user_input):
    factorial = 1
    for number in range(1, user_input + 1):
        factorial = factorial * number
    return factorial

def main():
    while True:
        user_input = get_input()
        check_is_digit = user_input.isdigit()
        check_is_char = user_input.isalpha()
        if(check_is_digit and (int(user_input) > 0)):
            factorial = calculate_factorial(int(user_input))
            print(f"The factorial of the given number {user_input} is {factorial}")
        elif(check_is_digit and (int(user_input) < 0)):
            print("Please enter the positive number")
            get_input()
            
main()