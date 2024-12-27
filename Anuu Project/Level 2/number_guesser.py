import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")
    
    # Get the range from the user
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound < upper_bound:
                break
            else:
                print("Please ensure the lower bound is less than the upper bound.")
        except ValueError:
            print("Please enter valid integers for the bounds.")

    # Generate a random number within the specified range
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"I have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")

    while True:
        # Prompt the user to enter a guess
        guess = input("Enter your guess (or type 'exit' to quit): ")

        # Allow the user to exit the game
        if guess.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break

        # Validate the input
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Provide hints based on the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Run the number guessing game
number_guesser()