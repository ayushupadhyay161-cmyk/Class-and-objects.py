# File-Handling- Problem: Employee Salary Filter create CSV file: employees.csv, emp_id,name, department, salary, 101, Ankit, IT,60000, 102, Sneha, HR,45000, 103, Ravi, IT, 75000
'''Tasks:
1) Create a class EmployeeManager
2) Read employee data from CSV
3) Filter employees whose salary is greater than 50,000
4) Create a JSON file
high_salary_employees.json
JSON should contain only emp_id, name, and salary.'''

# SOLUTION 

import csv
import json

csv_data = [
    ["emp_id", "name", "department", "salary"],
    [101, "Ankit", "IT", 60000],
    [102, "Sneha", "HR", 45000],
    [103, "Ravi", "IT", 75000]
]

with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = []

    def read_csv(self):
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.employees.append({
                    "emp_id": int(row['emp_id'].strip()),
                    "name": row['name'].strip(),
                    "department": row['department'].strip(),
                    "salary": int(row['salary'].strip())
                })

    def filter_and_save_json(self, output_filename):
        high_earners = [
            {
                "emp_id": emp["emp_id"], 
                "name": emp["name"], 
                "salary": emp["salary"]
            }
            for emp in self.employees if emp["salary"] > 50000
        ]

        with open(output_filename, 'w') as json_file:
            json.dump(high_earners, json_file, indent=4)
        
        print(f"File '{high_earners}' created successfully.")

manager = EmployeeManager('employee.csv')
manager.read_csv()
manager.filter_and_save_json('high_salary_employees.json')            
