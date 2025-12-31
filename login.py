# Login Validation System

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"

MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Validate empty inputs
    if username == "" or password == "":
        print("Error: Username and password cannot be empty.\n")
        continue

    # Check credentials
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\nLogin successful. Welcome!")
        break
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"Invalid credentials. Attempts remaining: {remaining}\n")
        else:
            print("\nAccount locked due to too many failed login attempts.")
