# Create a random name generator to generate a requested amount of random names for EC2 instances.

# Import necessary libraries
import random
import string   

# Welcome message
print("Welcome to the EC2 Instance Random Name Generator!")

department_names = input("Department Name: ")
number_of_ec2_names = int(input("Number of EC2 Names to Generate: "))

def generate_random_name(department, length=8):
    """Generate a random name for an EC2 instance."""
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{department}-{random_suffix}"
for _ in range(number_of_ec2_names):
    random_name = generate_random_name(department_names)
    print(f"Generated EC2 Instance Name: {random_name}")

