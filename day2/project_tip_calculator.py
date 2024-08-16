def main():
    print("Welcome to the Tip Calculator!")
    total_bill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    total_tip = total_bill * tip / 100
    total_bill += total_tip
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    final_amount = "{:.2f}".format(final_amount)
    print(f"Each person should pay: ${final_amount}")


if __name__ == '__main__':
    main()
