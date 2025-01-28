def check_balance(account_balance):
    print(f"Your balance is: {account_balance}")

def deposit(account_balance):
    print("Please Enter the amount you want to deposit: ")
    amount = int(input())
    account_balance = account_balance + amount
    return account_balance

def withdraw(account_balance):
    print("Please Enter the amount you want to deposit: ")
    amount = int(input())
    if(account_balance - amount < 0):
        print("Insufficiant Ammount")
    else:
        account_balance = account_balance - amount
        return account_balance

def main():
    account_balance = int(input("Enter your initial amount: "))
    while True:
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        print("Please choose the number to perform operation: ")
        n = int(input())
        if(n == 1):
            check_balance(account_balance)
        elif(n == 2):
            account_balance = deposit(account_balance)
        elif(n == 3):
            account_balance = withdraw(account_balance)
        elif(n == 4):
            break

main()