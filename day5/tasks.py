def print_for_loop():
    fruits = ["apple", "peach", "pear"]
    for fruit in fruits:
        print(fruit)


def scores():
    student_scores = [150, 142, 185, 170, 174, 171, 186, 191, 193, 195, 196, 199, 78, 90]
    total_exam_score = sum(student_scores)
    total_max_score = max(student_scores)
    my_sum = 0
    my_max = 0
    for score in student_scores:
        my_sum += score
        if score >= my_max:
            my_max = score
    print(f"Built-in sum: {total_exam_score}\nMy sum: {my_sum}\nBuilt-in max: {total_max_score}\nMy max: {my_max}")


def gauss_challenge():
    total = 0
    for number in range(1, 101):
        total += number
    print(total)


def fizzbuzz():
    for number in range(1, 101):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


if __name__ == '__main__':
    #print_for_loop()
    #scores()
    #gauss_challenge()
    fizzbuzz()
