# Practical Task 2: logic error program

# This program welcomes the user and gives a specific ticket price dependent on age
# the error is in the logic of the if statement deciding the ticket price

# declare variables

adult_ticket_age = 18
adult_ticket_price = "£20"
child_ticket_price = "£15"

# welcome user to the program
print("Hello there. Welcome to the logic error program")
print("")
print("There's a great band playing tonight!")

# ask user if they want a ticket
user_input = input("Would you like a ticket for the show? (y/n)").lower()

# if no, exit program
if user_input == "n":
    print("Okay, see you next time!")

# if yes, ask user age
elif user_input == "y":
    # get user age
    user_age = int(input("How old are you? (enter a number) "))

    # check user age meets requirement for adult ticket price or not

    if (
        adult_ticket_age > user_age
    ):  # a correct version of this logic would be: 'if (user_age >= adult_ticket_age):'
        # adult ticket message
        print(f"Okay, great big fella. That'll be {adult_ticket_price} please!")

    else:
        # child ticket message
        print(f"Okay, kiddo! That'll be {child_ticket_price} please!")
    print("Enjoy the show!")

# don't bother to ask again if the user enters something other than "y" or "n"
else:
    print("I didn't understand your input and I'm not going to ask again.")
