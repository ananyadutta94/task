def reverse_string(input_string):
    return input_string[::-1]

# Get user input
input_str = input("Enter a string to reverse: ")
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)