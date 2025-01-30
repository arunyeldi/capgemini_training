input_string = input("Enter the string for palindrome check: ")
if input_string == input_string[::-1]:
    print([input_string])
else:
    print("Not a palindrome")
