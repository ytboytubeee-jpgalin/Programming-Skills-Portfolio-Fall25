# ========================
# Basic Version
# ========================
# This will keep asking until the correct password ("12345") is entered.

CORRECT_PASSWORD = "12345"

print("=== Basic Password Entry (unlimited tries) ===")
while True:
    # If you prefer masking input (no visible text), uncomment the lines below and comment out the input() line.
    # from getpass import getpass
    # attempt = getpass("Enter password: ")
    attempt = input("Enter password: ")
    if attempt == CORRECT_PASSWORD:
        print("Access granted. Correct password entered.")
        break
    else:
        print("Incorrect password. Try again.")


# ========================
# Optional Version (max attempts)
# ========================
# This version limits the user to max_attempts tries.
# It informs the user how many attempts remain and alerts "authorities" after max attempts.

CORRECT_PASSWORD = "12345"
max_attempts = 5
attempts_left = max_attempts

print("\n=== Password Entry (maximum 5 attempts) ===")
while attempts_left > 0:
    # Uncomment to mask input:
    # from getpass import getpass
    # attempt = getpass("Enter password: ")
    attempt = input("Enter password: ")

    if attempt == CORRECT_PASSWORD:
        print("Access granted. Correct password entered.")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect password. Attempts remaining: {attempts_left}")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
            # (Optional) take any additional action here, e.g., log the event, lock account, etc.
