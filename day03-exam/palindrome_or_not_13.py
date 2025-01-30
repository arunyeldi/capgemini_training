#program to check whether the given string is palindrome or not

# function to input the value from the user
def get_input():
    given_input = input("Enter the string or a number (enter exit if you want to stop): ")
    return given_input

# function to check whether the given string is palindrome or not
def palindrome_check(given_input):
    given_input = str(given_input)
    given_input_reverse = given_input[::-1]
    if(given_input == given_input_reverse):
        return True
    else:
        return False

def main():
    # Taking input from the user until the user enters exit
    while True:
        given_input = get_input()
        if(given_input.lower() == 'exit'):
            print("Thank you...")
            break
        check = palindrome_check(given_input)
        if(check):
            print(f"The given string {given_input} is a palindrome...")
        else:
            print(f"The given string {given_input} is not a palindrome...")

main()