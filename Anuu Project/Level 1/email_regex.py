import re

def is_valid_email(email):
    # Define a regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the regex to match the email
    if re.match(email_regex, email):
        return True
    else:
        return False

# Get user input
email_input = input("Enter an email address to validate: ")

# Validate the email
if is_valid_email(email_input):
    print(f"{email_input} is a valid email address.")
else:
    print(f"{email_input} is not a valid email address.")