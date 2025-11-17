# Exercise 8: Simple Search

# --- Basic Version ---
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = "Sam"

if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")


# --- Optional Version ---
# Allow the user to input the search term
user_input = input("Enter the name you want to search for: ").strip()

if user_input in names:
    print(f"{user_input} was found in the list.")
else:
    print(f"{user_input} was not found in the list.")
