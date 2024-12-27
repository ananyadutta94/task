def count_word_occurrences(file_path):
    # Initialize a dictionary to hold word counts
    word_count = {}

    try:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            # Read the file content
            text = file.read()
            
            # Split the text into words (using whitespace as a delimiter)
            words = text.split()

            # Count occurrences of each word
            for word in words:
                # Normalize the word to lowercase and remove punctuation
                normalized_word = ''.join(char for char in word if char.isalnum()).lower()
                if normalized_word:  # Ensure the word is not empty
                    if normalized_word in word_count:
                        word_count[normalized_word] += 1
                    else:
                        word_count[normalized_word] = 1

        # Sort the dictionary by keys (words) and display the results
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the file path from the user
file_path = input("Enter the path to the text file: ")
count_word_occurrences(file_path)