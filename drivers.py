# Create a random name generator

# Import necessary libraries
import random
import string   

# Import the number of instances names are to be generated for
def import_instance_count():
    """Import the number of instances from user input."""
    while True:
        try:
            count = int(input("Enter the number of instance names to generate: "))
            if count > 0:
                return count
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.") 
            

# Import the number of names to be generated from user input
def generate_random_name(length=18):
    """Generate a random name of specified length."""
    letters = string.ascii_letters  # Include both uppercase and lowercase letters
    random_name = ''.join(random.choice(letters) for i in range(length))
    return random_name
# Example usage
if __name__ == "__main__":
    name_length = 18  # You can change this value to generate names of different lengths
    random_name = generate_random_name(name_length)
    print(f"Generated Random Name: {random_name}")  



