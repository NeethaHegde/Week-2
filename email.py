import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@([\w-]+\.)+[\w]{2,}$'
    return re.match(pattern, email) is not None

# Ask user to enter an email
email = input("Enter your email: ")

# Validate and show result
if is_valid_email(email):
    print("✅ Valid email.")
else:
    print("❌ Invalid email format.")
