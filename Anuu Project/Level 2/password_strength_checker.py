import re

def check_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Evaluate overall strength
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
        return "Moderate"
    else:
        return "Weak"

# Get user input
user_password = input("Enter a password to check its strength: ")
strength = check_password_strength(user_password)

print(f"The password strength is: {strength}")