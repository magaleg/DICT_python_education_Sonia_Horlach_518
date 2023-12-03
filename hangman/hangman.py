"""project Hangman"""

import random


def choose_word():
    """
    Chooses a word from the list "words".
    Returns:random word from the list.
    """
    words = ['python', 'java', 'javascript', 'php']
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Creates an empty string to show guessed letters or -s
    Parameters:
    word: is the word randomly chosen from the word list;
    guessed_letters: is the list of guessed letters from the word
    Returns:
    display string that contains guessed letters from the list or -s
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '-'
    return display


def hangman():
    """
    The main gameplay function. A player tries to guess letters
    from the randomly chosen word in list.

    word_to_guess is the randomly chosen word they have to guess.
    guessed_letters is the list of guessed letters.
    attempts is the general amount of their attempts. Isn't affected
    by errors related to the wrong letter case or symbols that aren't letters.

    Returns nothing.
    """
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 8

    print("HANGMAN")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Input your letter!>").lower()

        if len(guess) != 1:
            print("No, something's wrong. You should try just a single letter!")
            continue

        if not guess.isalpha():
            print("Just English *letters* will do!")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter, try another one!")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("That letter doesn't appear in the word!")
            attempts -= 1
        else:
            print("Done!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if '-' not in current_display:
            if attempts > 1:
                print("Congrats! you won!")
            else:
                print("Whew, that was your last attempt, but you won!")
            break

        if attempts == 0:
            print(f"Sorry, you lost. It was {word_to_guess}. Good luck next time!")
            break


def main_menu():
    """
    This function creates a simple menu for a player to choose between playing or exiting.
    """
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ').lower()

        if choice == 'play':
            hangman()
        elif choice == 'exit':
            print("Okay, see you!")
            break
        else:
            print("Wrong choice! Just 'play' or 'exit'")


if __name__ == "__main__":
    main_menu()

