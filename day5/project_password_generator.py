import random


def main():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
               '[', ']', '{', '}', ';', ':', '\\', '|', ',', '.', '<', '>', '/', '?', '~']
    number_of_letters = int(input("How many letter would you like in your password?\n"))
    number_of_symbols = int(input("How many symbols would you like?\n"))
    number_of_numbers = int(input("How many numbers would you like?\n"))

    # easy password with appending to the end
    '''
    password = ""
    for char in range(0, number_of_letters):
        password += random.choice(letters)
    for symbol in range(0, number_of_symbols):
        password += random.choice(symbols)
    for number in range(0, number_of_numbers):
        password += random.choice(numbers)
    print(password)
    '''

    # harder password with the randomizing of the easy password
    password_list = []
    for char in range(0, number_of_letters):
        password_list.append(random.choice(letters))
    for symbol in range(0, number_of_symbols):
        password_list.append(random.choice(symbols))
    for number in range(0, number_of_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = ''.join(password_list)
    print(f"Your password is: {password}")


if __name__ == '__main__':
    main()
