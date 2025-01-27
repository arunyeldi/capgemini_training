# Program to print the given pattern

# Here is the function to print the given pattern in reverse order
def print_pattern_in_reverse(number):
    for i in range(number, 0, -1):
            print("*" * (i))

# function to print the right angular triangle pattern
def print_pattern(number):
    for i in range(number):
        print("*" * (i + 1))
    
    # To print the given pattern in reverse order
    print("Do you want to print the pattern in reverse?")
    choice = input("Enter Yes or No: ")
    if(choice.lower() == 'yes'):
        print_pattern_in_reverse(number)
        print("Thank you..! Keep coding")
    else:
        print("Thank you..! Keep coding")

def main():
    print("***Program to print the pattern***")
    number = int(input("Enter the Number: "))
    print_pattern(number)

main()