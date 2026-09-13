import random

WORDS = [
    "python", "hangman", "keyboard", "developer", "function",
    "variable", "computer", "network", "algorithm", "database",
    "internet", "software", "hardware", "terminal", "notebook"
]

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]

MAX_WRONG_GUESSES = len(HANGMAN_PICS) - 1


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another.")
        else:
            return guess


def play_round():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_PICS[wrong_guesses])
        print(display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou won! The word was '{word}'.")
            return True

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Wrong guess!")
        else:
            print("Correct!")
        print()

    print(HANGMAN_PICS[wrong_guesses])
    print(f"You lost! The word was '{word}'.")
    return False


def main():
    print("Welcome to Hangman!")
    wins = 0
    losses = 0

    while True:
        won = play_round()
        if won:
            wins += 1
        else:
            losses += 1

        print(f"\nScore — Wins: {wins}  Losses: {losses}")
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
