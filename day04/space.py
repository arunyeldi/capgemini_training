list_items = []
str = ""
s = input("Enter the string: ")
new_str = ""
c = 0
for i in s:
    if i == ' ':
        # if c == 0:
        #     c += 1
        #     new_str += ' '
        continue
    else:
        new_str += i
        c = 0
list_items = list(new_str.split())
for i in list_items:
    if i == i[::-1]:
        print(f"{i} is Palindrome")
    else:
        print(f"{i} is not Palindrome")
