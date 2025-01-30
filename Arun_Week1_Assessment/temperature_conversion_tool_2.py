# Temperature Conversion Tool

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def display_menu():
    print("\nTemperature Conversion Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option between (1-7): ")
        
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F.")
        
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius:.2f}°C is {kelvin:.2f}K.")
        
        elif choice == '3':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C.")
        
        elif choice == '4':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit:.2f}°F is {kelvin:.2f}K.")
        
        elif choice == '5':
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin:.2f}K is {celsius:.2f}°C.")
        
        elif choice == '6':
            kelvin = float(input("Enter temperature in Kelvin: "))
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin:.2f}K is {fahrenheit:.2f}°F.")
        
        elif choice == '7':
            print("Exiting the temperature conversion tool. Thank you!")
            break
        
        else:
            print("Invalid option. Please choose a valid menu number.")

main()
