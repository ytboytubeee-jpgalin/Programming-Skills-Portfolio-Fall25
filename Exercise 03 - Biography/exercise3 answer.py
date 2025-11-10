# Exercise 3: Biography

# --- Basic Version ---
# Storing hardcoded information in a dictionary
bio = {
    "name": "Alin Muhmmed",
    "hometown": "Dubai",
    "age": 19
}

# Printing the values on separate lines using one print statement
print(bio["name"], bio["hometown"], bio["age"], sep="\n")

# --- Advanced Version ---
# Getting user input for the biography
name = input("Enter your full name: ")          # Handles multiple words (e.g., 'Alin Muhmmed')
hometown = input("Enter your hometown: ")

# Using try-except to handle invalid (non-numeric) age input
try:
    age = int(input("Enter your age: "))        # Converts to integer
except ValueError:
    print("Invalid input for age! Please enter a number.")
    age = None

# Creating a dictionary with the user-provided information
user_bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Printing the user’s biography
print("\n--- Biography ---")
print(user_bio["name"], user_bio["hometown"], user_bio["age"], sep="\n")
