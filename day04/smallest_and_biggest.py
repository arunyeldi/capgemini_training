
list_items = [int(input(f"Enter number {i + 1} : ")) for i in range(5)]
mini = float('inf')
maxi = -float('inf')
for i in list_items:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print(f"Smallest number is: {mini}" )
print(f"Largest number is: {maxi}" )