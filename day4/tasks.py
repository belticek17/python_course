import random


def random_numbers():
    random_int = random.randint(1, 10)
    random_float = random.random() * 5
    love_score = random.randint(1, 100)
    print(random_int, random_float, love_score)


def heads_or_tails():
    if random.randint(0, 1) == 1:
        print("Heads")
    else:
        print("Tails")


def states_of_america():
    states = ["Delaware", "Pennsylvania"]
    states[1] = "Pencilvania"
    states.append("AngelaLand")
    states.extend(["JurajLand", "AnnaLand"])
    print(states[len(states)-1])


def bill():
    friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
    print(random.choice(friends))


def main():
    random_numbers()
    heads_or_tails()
    states_of_america()
    bill()


if __name__ == '__main__':
    main()