import random
from words_list import words
from hangman_art import stages


def main():
    # List of stages
    number_of_lives = 6

    chosen_word = random.choice(words)

    placeholder = ''
    for i in range(len(chosen_word)):
        placeholder += '_'
    print(placeholder)

    game_over = False
    correct_letters = []

    while not game_over:
        print(f"***************You have {number_of_lives} incorrect guesses left!***************")
        my_guess = input("Guess a letter: ").lower()

        if my_guess in correct_letters:
            print(f"***************You have already guessed {my_guess}!***************")

        display = ''
        for char in chosen_word:
            if my_guess == char:
                display += char
                correct_letters.append(char)

            elif char in correct_letters:
                display += char

            else:
                display += '_'

        print(stages[number_of_lives])
        print(display)

        if my_guess not in chosen_word:
            number_of_lives -= 1
            print(f"***************You guessed {my_guess}, that's not in the word so you lose a life!***************")
            if number_of_lives == 0:
                game_over = True
                print(stages[number_of_lives])
                print(f"***************You lost! The correct word was {str(chosen_word).capitalize()}!***************")

        if '_' not in display:
            game_over = True
            print(f"***************You won! The correct word was {str(chosen_word).capitalize()}!***************")


if __name__ == '__main__':
    main()