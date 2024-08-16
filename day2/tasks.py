def two_digit_number():
    number = input()
    first_digit = int(number[0])
    second_digit = int(number[1])
    result = first_digit + second_digit
    print(result)


def bmi_calculator():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    bmi = weight / height ** 2
    print(int(bmi))


def life_in_weeks():
    age = int(input("What is your current age? "))
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 12
    print(f"You have {weeks_remaining} weeks left.")


def errors():
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    print("Hello, " + name + "!")
    age = 12
    print(f"Your are {age} years old.")
    print("You are " + str(age) + " years old.")


if __name__ == '__main__':
    #two_digit_number()
    #bmi_calculator()
    #life_in_weeks()
    errors()
