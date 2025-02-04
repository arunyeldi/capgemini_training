def add_item(dictionary):
    item = input("Enter the item name: ")
    value = int(input("Enter the price of the item: "))
    dictionary[item] = value

def view_cart(dictionary):
    if not dictionary:
        print("Cart is empty")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def calculate_price(dictionary):
    total_price = sum(dictionary.values())
    print(f"Total price: {total_price}")

def main():
    dictionary = {}
    while True:
        print("1. Add item to the cart")
        print("2. View cart items")
        print("3. Calculate the total price")
        print("4. Exit")
        n = int(input("Enter the number (which operation to perform?): "))
        if(n == 1):
            add_item(dictionary)
        elif(n == 2):
            view_cart(dictionary)
        elif(n == 3):
            total_price = calculate_price(dictionary)
            print(f"Total price of the cart = {total_price}")
        elif(n == 4):
            print("Exiting the shopping cart. Thank you!")
            break

main()