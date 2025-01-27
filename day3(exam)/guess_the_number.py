import random
def main():
    random_number = random.randint(1, 100)
    print(random_number)
    while True:
        a = int(input("Enter the number (Enter 0 to exit): "))
        if(a == 0):
            break
        elif(a == random_number):
            print("Congratulations... You are correct...")
            break
        elif(a < random_number):
            print("Oops...! Too Low Try again")
            continue
        elif(a > random_number):
            print("Oops...! Too High Try again")
            continue

main()