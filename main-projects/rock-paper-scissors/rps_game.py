# This is a rock paper scissors game to practice using variables in an if statement as well as
# getting user input and importing a random number function.

import random

# sets the viable options for the game
options = ["rock", "paper", "scissors"]

# sets the scores
user_score = 0
comp_score = 0

# sets the play state to "y"
playing = "y"
print("")
print("Welcome to the game!")
print("")

# continues to run new games while state is "y"
while playing == "y":
    # get user input for the game
    user_input = input("Choose rock, paper or scissors: ").lower()
    # get a random choice from the PC player
    comp_choice = random.choice(options)

    # loop until the user choices a valid option
    while user_input not in options:
        print("Invalid choice. Please enter another option")
        user_input = input("Choose rock, paper or scissors: ").lower()

    # print user's choice
    print("You have chosen " + user_input)
    # print PC choice
    print("Comp has chosen " + comp_choice)

    # various outcomes
    if user_input == comp_choice:
        print("It's a draw!")
    elif user_input == "rock" and comp_choice == "scissors":
        user_score += 1
        print("You win!")
    elif user_input == "paper" and comp_choice == "rock":
        user_score += 1
        print("You win!")
    elif user_input == "scissors" and comp_choice == "paper":
        user_score += 1
        print("You win!")
    elif user_input == "rock" and comp_choice == "paper":
        comp_score += 1
        print("You lose!")
    elif user_input == "paper" and comp_choice == "scissors":
        comp_score += 1
        print("You lose!")
    elif user_input == "scissors" and comp_choice == "rock":
        comp_score += 1
        print("You lose!")
    else:
        print("Unknown outcome!")

    # new line
    print("")
    # display scores
    print(f"The score is: ")
    print(f"User: {user_score} | Computer: {comp_score}")

    # display who is winning overall
    if user_score == comp_score:
        print("It's tied overall!")
    elif user_score > comp_score:
        print("You're winning overall!")
    else:
        print("The Computer is winning overall!")
    # asks user if they'd like to keep playing
    playing = str(input("Continue playing (Y/N)? ").lower())

    # check response is valid
    while playing != "y":
        # if answer is "n". say goodbye and end game loop
        if playing == "n":
            print("")
            # display who is winning overall
            if user_score == comp_score:
                print("It's tied overall!")
            elif user_score > comp_score:
                print("You win overall!")
            else:
                print("The Computer wins overall!")

            # goodye message
            print("Thanks for playing! GoodBye!")
            # end loop
            break

        # if answer is invalid, ask again
        else:
            print("Unrecognised input. Please try again.")
            playing = str(input("Continue playing (Y/N)? ").lower())

    # if answer is "y", print new line and restart game loop
    else:
        print("")
