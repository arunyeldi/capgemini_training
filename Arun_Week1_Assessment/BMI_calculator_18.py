# BMI Calculator program

# function to display the category to which the person belongs to and provides suggestion accordingly
def display(BMI_value):
    if(BMI_value < 18.5):
        print("You are Underweight")
        print("Suggestion: Maintain a balanced diet daily and intake high protein food such as meat")
    elif(BMI_value >= 18.5 and BMI_value <= 24.9):
        print("You are Normal weight")
        print("Suggestion: Maintain a balanced diet daily and intake high protein food such as meat")
    elif(BMI_value >= 25 and BMI_value <= 29.9):
        print("You are Overweight")
        print("Suggestion: Please avoid junk food and Keep Exercising daily")
    else:
        print("You are Obese")
        print("Suggestion: Please avoid junk food and Keep Exercising daily")

# function to take the weight and height from the user
def get_input():
    weight = int(input("Please provide us your body weight in kilograms: "))
    height = int(input("Please provide us your height in centimeters: "))
    return (weight, height)

# function to calculate the BMI value
def calculate_BMI(weight, height_in_meters):
    BMI_value = weight / (height_in_meters * height_in_meters)
    return BMI_value

def main():
    print("\n* * * Program to calculate the BMI * * *\n")
    (weight, height) = get_input()
    height_in_meters = height / 100
    BMI_value = calculate_BMI(weight, height_in_meters)
    display(BMI_value)

main()