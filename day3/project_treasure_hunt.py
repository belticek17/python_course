def main():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    print('You\'re at a crossroad. Where do you want to go? Type "left" or "right"')
    direction = input().lower()

    if direction == 'left':
        activity = input(f"You went {direction} and have come to a lake, there is an island in the middle of it."
                         f"Type \"wait\" to wait for a boat or type \"swim\" to swim across. ")
        if activity == 'wait':
            door_colour = input(f"You opted to {activity} for a boat and arrived at the island unharmed."
                                f" There is a house with 3 doors."
                                f"The 1st one is blue, the 2nd one is red and, the last one is yellow."
                                f"Which colour do you choose? ").lower()
            if door_colour == 'yellow':
                print(f"You opened the {door_colour} door. You win!")
            elif door_colour == 'red':
                print(f"You opened the {door_colour} door. You burned alive. Game over!")
            elif door_colour == 'blue':
                print(f"You opened the {door_colour} door. You were eaten by a beast. Game over!")
            else:
                print("Invalid move. Game over!")
        elif activity == 'swim':
            print("You were attacked by an angry trout and drowned. Game over!")
        else:
            print("Invalid move. Game over!")
    elif direction == 'right':
        print("You fell into a hole. Game over!")
    else:
        print("Invalid move. Game over!")


if __name__ == '__main__':
    main()
