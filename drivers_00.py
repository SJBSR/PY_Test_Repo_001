# Create a random name generator to generate a requested amount of random names for EC2 instances.

# Import necessary libraries
import random
import string   

# Welcome message
print("Welcome to the EC2 Instance Random Name Generator!")

# Prompt the user to input their department name
department_names = input("Department Name: ")

# Prompt the user to input the number of EC2 instance names to generate
number_of_ec2_names = int(input("Number of EC2 Names to Generate: "))

# Define a function named 'generate_random_name' that takes 'department' (required) and 'length' (optional, default 8) as arguments
def generate_random_name(department, length=8):
    # Generate a random alphanumeric string of a specified length and join the characters
    """Generate a random name for an EC2 instance."""
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    # Return the department name concatenated with a hyphen and the random suffix using an f-string
    return f"{department}-{random_suffix}"
# Loop 'number_of_ec2_names' times (the loop variable '_' is a convention for an unused variable)
for _ in range(number_of_ec2_names):
    # Call the 'generate_random_name' function with the user's department input and store the result
    random_name = generate_random_name(department_names)
    # Print the generated EC2 instance name to the console using an f-string
    print(f"Generated EC2 Instance Name: {random_name}")

