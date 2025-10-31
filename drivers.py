# Create a random word generator

#Import necessary libraries
import random
import string   

#import the length of the word from user
def generate_random_word(length):length = int(length)

#Generate a random word of given length
length = int(input("Enter the length of the random word: "))

# Define data to be used in the password generation
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase

# Combine the data to form the character set
character_set = lowercase_letters + uppercase_letters

