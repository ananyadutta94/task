def fibonacci_sequence(n):
    # Initialize the first two terms of the Fibonacci sequence
    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Update to the next terms in the sequence

    return fib_sequence

# Get user input
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if num_terms < 0:
        print("Please enter a non-negative integer.")
    else:
        sequence = fibonacci_sequence(num_terms)
        print(f"The Fibonacci sequence up to {num_terms} terms is: {sequence}")
except ValueError:
    print("Please enter a valid integer.")