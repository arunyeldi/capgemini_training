# Program to separate the numbers of a single list into odd even lists 

# function to display the odd list and even list
def display(odd, even):
    print(f"Odd list: {odd}")
    print(f"Even list: {even}")

# function to create a list of n elements
def get_input_list(number):
    input_list = []
    # taking inputs and add the elements to the list until the for loop completes
    for i in range(number):
        input_number = int(input(f"Enter number {i + 1}: "))
        input_list.append(input_number)
    return input_list

# function to separate the odd and even list
def odd_even_separator(input_list):
    odd = [] # an empty list to store the odd numbers
    even = [] # an empty list to store the even numbers
    for i in input_list:
        # check the value is even of not
        if i % 2 == 0:
            # append method adds the value to the end of the list
            even.append(i)
        else:
            odd.append(i)
    return (odd, even)

def main():
    print("* * * Program to separate the a single list into odd even lists * * *")
    print("Enter the number (Number of elements to store in the list): ", end = "")
    number = int(input())
    input_list = get_input_list(number) # calling function get input list 
    (odd, even) = odd_even_separator(input_list) # calling function odd even separator to separate the list
    display(odd, even) # calling display function to display the separated odd even lists

main()