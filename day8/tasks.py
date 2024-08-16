def greet():
    print("Hello world!")
    print("Hello Juraj!")
    print("Hello Udemy!")


def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How are you {name}?")
    print(f"What's the time {name}?")


def life_in_weeks(age):
    my_age = age
    years_remaining = 90 - my_age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")


def calculate_love_score(name1, name2):
    both_names = name1 + name2
    lower_names = both_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")

    first_digit = t + r + u + e
    second_digit = l + o + v + e
    score = int(str(first_digit) + str(second_digit))
    print(score)


def main():
    greet()
    greet_with_name("Juraj")
    life_in_weeks(int(input("My age is ")))
    greet_with("Juraj", "Hnúšťa")
    greet_with(name="Anna", location="Gánovce")
    calculate_love_score("Kanye West", "Kim Kardashian")


if __name__ == '__main__':
    main()
