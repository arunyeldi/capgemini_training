# Program to check the given year is a leap year or not

def get_input():
    year = int(input("Enter the year to check leap year or not: "))
    return year

def main():
    while True:
        year = get_input()
        if ((year % 100 != 0) and (year % 4 == 0)) or (year % 400 == 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")

main()