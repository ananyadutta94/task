import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

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

# Run the guessing game
guessing_game()