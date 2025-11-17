# Exercise 10: Is it even?

def check_even_odd(number):
    """
    Function to determine if a number is even or odd.
    Returns a message string.
    """
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    try:
        # Ask the user for a number
        num = int(input("Enter a number: "))
        
        # Pass the number to the function
        result = check_even_odd(num)
        
        # Print the result
        print(result)
        
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
