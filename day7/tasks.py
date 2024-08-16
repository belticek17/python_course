import random


def main():
    # Define each stage of Hangman as a string
    stages = ["""
    ------
    |    |
    |    O
    |   /|\\
    |    |
    |   / \\
    |
    |
    |
    ----------
    """, """
    ------
    |    |
    |    O
    |   /|\\
    |    |
    |   /
    |
    |
    |
    ----------
    """, """
    ------
    |    |
    |    O
    |   /|\\
    |    |
    |
    |
    |
    |
    ----------
    """, """
    ------
    |    |
    |    O
    |   /|
    |    |
    |
    |
    |
    |
    ----------
    """, """
    ------
    |    |
    |    O
    |    |
    |    |
    |
    |
    |
    |
    ----------
    """, """
    ------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
    ----------
    """, """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """]

    # List of stages
    number_of_lives = 6

    word_list = ['aardvark', 'baboon', 'camel']
    chosen_word = random.choice(word_list)

    placeholder = ''
    for i in range(len(chosen_word)):
        placeholder += '_'
    print(placeholder)

    game_over = False
    correct_letters = []

    while not game_over:
        print(f"You have {number_of_lives} incorrect guesses left!")
        my_guess = input("Guess a letter: ").lower()

        display = ''
        for char in chosen_word:
            if my_guess == char:
                display += char
                correct_letters.append(char)

            elif char in correct_letters:
                display += char

            else:
                display += '_'

        print(display)

        if my_guess not in chosen_word:
            number_of_lives -= 1

        if '_' not in display:
            game_over = True
            print(f"You won! The correct word was {chosen_word}!")

        if number_of_lives == 0:
            game_over = True
            print(f"You lost! The correct word was {chosen_word}!")

        print(stages[number_of_lives])


if __name__ == '__main__':
    main()
