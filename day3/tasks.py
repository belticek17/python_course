def rollercoaster():
    print("Welcome to the Rollercoaster!")
    height = int(input("What is your height in cm? "))
    bill = 0

    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))
        if age < 12:
            print("Child tickets are $5.")
            bill = 5
        elif age <= 18:
            print("Youth tickets are $7.")
            bill = 7
        elif age >= 45 and age <= 55:
            print("Everything is going to be ok. Have a free ride on us!")
        else:
            print("Adult tickets are $12.")
            bill = 12
        photos = input("Do you want a photo taken? Y or N. ")
        if photos == 'Y':
            bill += 3

        print(f"Your total bill is ${bill}")
    else:
        print("Sorry, you have to grow taller before you can ride!")


def even_or_odd():
    if int(input()) % 2 == 0:
        print("EVEN NUMBER")
    else:
        print("ODD NUMBER")


def bmi_2_point_0():
    height = float(input("How tall are you in m? "))
    weight = float(input("How much do weigh in kg? "))

    bmi = weight / height ** 2
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")


def leap_year():
    year = int(input("Write the year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")


def pizza_order():
    print("Thank you for choosing Python Pizza Deliveries!")
    size = input()  # What size pizza do you want? S, M, or L
    add_pepperoni = input()  # Do you want pepperoni? Y or N
    extra_cheese = input()  # Do you want extra cheese? Y or N
    if size == 'S':
        price = 15
        if add_pepperoni == 'Y':
            price += 2
    elif size == 'M':
        price = 20
        if add_pepperoni == 'Y':
            price += 3
    else:
        price = 25
        if add_pepperoni == 'Y':
            price += 3

    if extra_cheese == 'Y':
        price += 1

    print(f"Your final bill is: ${price}.")


def love_calculator():
    name1 = input("What is your name? ")
    name2 = input("What is the name of your crush? ")
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

    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif 40 < score < 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")


if __name__ == '__main__':
    #rollercoaster()
    #even_or_odd()
    #bmi_2_point_0()
    #leap_year()
    #pizza_order()
    love_calculator()
