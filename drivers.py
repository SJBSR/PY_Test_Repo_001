# Create a random name generator

# Import necessary libraries
import random
import string   

# Request user input for the number of names to be generated
def input_amount_of_names():
    while True:
        try:
            amount = int(input("Enter the number of random names to generate: "))
            if amount <= 0:
                print("Please enter a positive integer.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to generate a random string name
def generate_random_string_name(length=18):
    """Generate a random name of specified length consisting only of ASCII letters."""
    letters = string.ascii_letters  # Include both uppercase and lowercase letters
    random_name = ''.join(random.choices(letters, k=length))
    return random_name
# Example usage: Generate and print the number of random names specified by the user
if __name__ == "__main__":
    amount = input_amount_of_names()
    name_length = 18  # You can change this value to generate names of different lengths
    for i in range(amount):
        random_name = generate_random_string_name(name_length)
        print(f"Generated Random Name {i+1}: {random_name}")

# Function to generate a random name
def function_generate_name():
    return generate_random_string_name()

