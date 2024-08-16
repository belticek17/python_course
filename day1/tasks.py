def print_all_lines():
    print(
        "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n"
        "2. Knead the dough for 10 minutes.\n"
        "3. Add 3g of Salt.\n"
        "4. Leave to rise for 2 hours.\n"
        "5. Bake at 200 degrees C for 30 minutes.")

    print('She said: "Hello" and then left.')
    print("She said: \"Hello\" and then left.")


def debug():
    # Fix the code below 👇

    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")


def input_function():
    name = input("What's your name? ")
    print("Hello " + name + "!")
    print(len(name))


def switch_values():
    a = input("a: ")
    b = input("b: ")

    c = a
    a = b
    b = c

    print("a: " + a)
    print("b: " + b)


if __name__ == "__main__":
    print_all_lines()
    debug()
    input_function()
    switch_values()
