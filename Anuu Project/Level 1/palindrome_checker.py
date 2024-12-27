def is_palindrome(input_string):
    # Normalize the string by removing spaces and converting to lowercase
    normalized_string = ''.join(input_string.split()).lower()
    
    # Check if the normalized string is equal to its reverse
    return normalized_string == normalized_string[::-1]

# Get user input
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')