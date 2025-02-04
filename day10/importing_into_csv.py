import csv


input_file = 'input_details.csv'   
output_file = 'output_details.csv'

employee_details = [['emplyee_name', 'employee_id', 'employee_salary']]
employee_name = input('Enter employee name: ')
employee_id = input('Enter employee ID: ')
employee_salary = int(input("Enter employee salary: "))
employee_details.append([employee_name, employee_id, employee_salary])

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile_details:
    reader = csv.reader(infile)
    writer = csv.writer(outfile_details)
    
    headers = next(reader)  # Read the first line as headers
    writer.writerow(headers)
    
    
    for row in reader:
        if row != headers:
            writer.writerow(row)

print(f"Processed file saved as '{output_file}'.")
