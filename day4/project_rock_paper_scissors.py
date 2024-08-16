import random
def main():
    choices = ["Rock", "Paper", "Scissors"]
    my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors!\n"))
    computer_choice = random.choice(choices)
    if my_choice == 0:
        print(f"You chose: {choices[0]}")
        my_choice = choices[0]
    elif my_choice == 1:
        print(f"You chose: {choices[1]}")
        my_choice = choices[1]
    elif my_choice == 2:
        print(f"You chose: {choices[2]}")
        my_choice = choices[2]
    else:
        print("Error!")

    print(f"Computer chose: {computer_choice}")
    if my_choice == computer_choice:
        print("It's a draw!")
    elif ((my_choice == "Rock" and computer_choice == "Paper")
          or (my_choice == "Paper" and computer_choice == "Scissors")
          or (my_choice == "Scissors" and computer_choice == "Rock")):
        print("You lose!")
    else:
        print("You win!")


if __name__ == '__main__':
    main()
