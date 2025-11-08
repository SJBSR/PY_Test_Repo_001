# Create a random name generator to generate a requested amount of random names for EC2 instances.

import random
import string

print("Welcome to the EC2 Instance Name Generator!")

# Dictionry of allowed department names
# Keys are dept name, values are acceptable user inputs
allowed_departments_dict = {"ACC": ["Accounting", "ACCOUNTING", "accounting", "ACC", "acc", "Acc"],
                       "FIN": ["Finance", "FINANCE", "finance", "FIN", "fin", "Fin"],
                       "MKT": ["Marketing", "MARKETING", "marketing", "MKT", "mkt", "Mkt"]}
# Values are acceptable user inputs

# Define vals
vals = allowed_departments_dict.values()
key = allowed_departments_dict.keys()

# Function to validate department name input
def department_name_input():
    """Prompt the user to input and validate their department name."""
    while True:
        dept = input("Department Name: ").strip()
        if not dept:
            print("Department name cannot be empty. Please try again.")
        elif dept.isdigit():
            print("Department name cannot be numeric. Please try again.")
        elif any(dept in values for values in allowed_departments_dict.values()):
            for key, vals in allowed_departments_dict.items():
                if dept in vals:
                    dept = key
            return dept
        else:
            print("Your department is not allowed to use this name generator, contact your admin for assistance.")

# Function to validate number of names input
def amount_of_names_input():
    """Prompt the user to input and validate the number of EC2 names to generate."""
    while True:
        try:
            num = int(input("Number of EC2 Names to Generate: "))
            if num <= 0:
                print("The number of EC2 names must be a positive integer. Please try again.")
            elif num > 100:
                print("The number of EC2 names cannot exceed 100. Please try again.")
            else:
                return num
        except ValueError:
            print("Please enter a valid integer.")

department_names = department_name_input()
number_of_ec2_names = amount_of_names_input()
def generate_random_name(department, length=8):
    """Generate a random name for an EC2 instance."""
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return f"{department}-{random_suffix}"
for _ in range(number_of_ec2_names):
    random_name = generate_random_name(department_names)
    print(f"Generated EC2 Instance Name: {random_name}")
