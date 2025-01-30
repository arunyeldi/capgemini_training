l = []
for i in range(5):
    a = int(input(f"Enter the number {i + 1}: "))
    l.append(a)
print("Sum of list: ", sum(l))
print("Average of list: ", sum(l) / len(l))