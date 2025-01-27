# Student Grading System

def calculate_total_and_percentage(marks):
    total_marks = sum(marks)
    percentage = total_marks / len(marks)
    return total_marks, percentage

def get_grade(percentage):
    if percentage >= 85:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'Fail'

def main():
    student_name = input("Enter the student's name: ")
    marks = []
    for i in range(1, 6):
        mark = input(f"Enter marks for subject {i} (0-100): ")
        mark = float(mark)
        if 0 <= mark <= 100:
            marks.append(mark)
        else:
            print("Please enter a valid mark between 0 and 100.")
            i -= 1

    total_marks, percentage = calculate_total_and_percentage(marks)

    grade = get_grade(percentage)
    
    print("\n--- Student Report ---")
    print(f"Student Name: {student_name}")
    print(f"Total Marks: {total_marks:.2f} / 500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

main()
