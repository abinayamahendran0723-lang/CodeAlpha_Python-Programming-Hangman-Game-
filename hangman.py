import random

WORDS = ["python", "keyboard", "network", "database", "function"]
MAX_WRONG = 6


def display_word(word, guessed):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []   # all letters guessed so far
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word, one letter at a time. You have {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print("Word:", display_word(word, guessed))
        print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "none")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

        # Win check: every letter in the word has been guessed
        if all(letter in guessed for letter in word):
            print("Word:", display_word(word, guessed))
            print(f"Congratulations! You guessed the word '{word}'!")
            return

    print(f"Game over! The word was '{word}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
