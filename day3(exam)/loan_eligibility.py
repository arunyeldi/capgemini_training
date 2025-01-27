def main():
    salary = int(input("Enter salary: "))
    age = int(input("Enter age: "))
    credit_score = int(input("Enter credit score: "))
    if(salary >= 50000 and age >= 21 and credit_score >= 700):
        print("You are eligible for loan approval")
    else:
        print('You are not eligible for loan approval')

main()