l1 = []
print("\nEmpty list: ", l1)

l2 = [1, 2, 3, 'Python']
print("List of four items", l2)

l3 = [2, '4', ['Python, list']]
print("Nested List", l3)

l4 = list('spam')
print("list created from string 'spam'", l4)

l5 = list(range(-4, 4))
print("list created from range(-4, 4): ", l5)

l6 = [1, 2, 3, 4, 5]
print("Element at index 3: ", l6[3])

l7 = [1, 2, 3, [12, 23, 45]]
print("Accessing element from nested list: ", l7[3][1])

l8 = [10, 20, 30, 40, 50, 60]
print("List slicing: ", l8[2 : 5])

l9 = [0, 1, 2, 3, 4, 5, [10, 20, 30]]
print("Length of list: ", len(l9))
print("Slice the sublist: ", l9[6][1:3])

