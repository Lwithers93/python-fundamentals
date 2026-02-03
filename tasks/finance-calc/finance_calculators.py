# Capstone Project

import math

# display options to user
print("Options:")
print(
    "investment - to calculate the amount of interest you'll earn on your investment"
)
print(
    "bond       - to calculate the amount you'll have to pay on a home loan"
)

print("")

# ask user to choose on of the displayed options and convert input to lower case
user_input = input(
    "Enter either 'investment' or 'bond' from the menu above to proceed: "
).lower()

# check user has provided valid response and re-request if not
while user_input:
    if user_input == "investment" or user_input == "bond":
        break
    else:
        print("Invalid option. Please try again.")
        user_input = input(
            "Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

print("")

# print user response
print("You have selected " + user_input)

if user_input == "investment":

    # get deposit amount
    deposit = float(input("How much money are you depositing? "))

    # get interest rate, remove "%" if given, divide by 100
    rate = (float(
        input("What percentage interest rate do you have? ").replace("%", "")))/100

    # get length of investment
    length = int(input("How many years are you investing for? "))

    # get the interest type, i.e. "simple" or "compound"
    interest = input("Do you want simple or compound interest? ")

    # check valid interest type, try again if not
    while interest != "":
        if interest == "simple" or interest == "compound":
            break
        else:
            print("Invalid option. Please try again.")
            interest = input(
                "Do you want simple or compound interest? ").lower()

    # begin calculations
    if interest == "simple":
        new_amount = deposit * (1 + (rate * length))
        print(
            f"The new amount after simple interest investment across {length} years at {rate}% is: {round(new_amount,2)}")
    elif interest == "compound":
        new_amount = deposit * math.pow((1+rate), length)
        print(
            f"The new amount after compound interest investment across {length} years at {rate}% is: £{round(new_amount,2)}")

elif user_input == "bond":

    # get house value
    value = int(input("What is the current value of your house? "))

    # get interest rate, remove "%" if given, divide by 100
    rate = (float(
        input("What percentage interest rate do you have? ").replace("%", "")))/100

    # get length of investment
    length = int(input("How many months will you repay the bond over? "))

    # calculate monthly repayments
    repayment = (rate * value)/(1-(1+rate)**(-length))
    print(
        f"The  amount to be repaid each month (for {length} months) is: £{round(repayment,2)}")
