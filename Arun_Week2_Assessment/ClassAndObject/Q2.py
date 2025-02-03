class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print(f"\nYour account balance is: {self.balance}\n")

    def deposit(self):
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        self.balance += deposit_amount
    
    def withdraw(self):
        withdraw_amount = int(input("Enter the amount you want to withdraw: "))
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
        else:
            print("\nInsufficient Balance\n")
    
initial_balance = 0
bank_account = BankAccount(initial_balance)

while True:
    print("* * * Designing BankAccount * * *")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Display Balance")
    user_input = input("\nEnter the number: ")
    if user_input == '1':
        bank_account.deposit()
    elif user_input == '2':
        bank_account.withdraw()
    elif user_input == '3':
        bank_account.display()
    else:
        print("\nPlease enter the valid number\n")

    
    