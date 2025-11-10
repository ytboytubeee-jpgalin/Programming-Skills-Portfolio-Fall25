# Exercise 5: Days of the Month

# Step 1: Create a dictionary mapping month numbers to number of days
month_days = {
    1: 31,  # January
    2: 28,  # February (default, can adjust for leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Step 2: Ask the user for the month number
try:
    month = int(input("Enter the month number (1-12): "))
    
    # Step 3: Check if input is valid
    if month < 1 or month > 12:
        print("Invalid month number! Please enter a number between 1 and 12.")
    else:
        # Advanced Requirement: Leap year adjustment for February
        if month == 2:
            leap = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap == "yes":
                days = 29
            else:
                days = 28
        else:
            days = month_days[month]
        
        print(f"Month {month} has {days} days.")
except ValueError:
    print("Invalid input! Please enter a numeric value for the month.")
