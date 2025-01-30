# program to find the second largest number in a list

def main():
    n = int(input())
    l = []
    for i in range(n):
        a = int(input())
        l.append(a)
    first_largest = 0
    second_largest = 0
    for i in l:
        if i > first_largest:
            first_largest = i
    for i in l:
        if i > second_largest and i < first_largest:
            second_largest = i
    print(second_largest)

main()