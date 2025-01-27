def check_balance(money):
    print(money)

def deposit(money):
    print("Please Enter the amount you want to deposit: ")
    amount = int(input())
    money = money + amount
    return money

def withdraw(money):
    print("Please Enter the amount you want to deposit: ")
    amount = int(input())
    money = money - amount
    return money

def main():
    money = 0
    while True:
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        print("Please enter the number: ")
        n = int(input())
        if(n == 1):
            check_balance(money)
        elif(n == 2):
            money = deposit(money)
        elif(n == 3):
            money = withdraw(money)
        elif(n == 4):
            break

main()