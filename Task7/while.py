# Practical Task One

# pseudo code

# declare empty list variable to store user inputs
# begin loop
# ask user to input number
# if number is not -1, add it to the list and restart loop
# if number is -1 stop loop. Do NOT add -1 to list
# calculate average of numbers in list
# print output

# code

# declare empty list variable
my_list = []

# declare user input variable
user_input = 0

# start loop if user input is not equal to -1
while user_input != -1:
    # get user input
    user_input = int(input("Please enter a whole number: "))
    if user_input != -1:
        # add user input to the list if NOT -1
        my_list.append(user_input)
        print("User input is not -1. User input has been added to list!")

    # else statement not necessarily required but included anyway
    else:
        print("User input is -1! Ending the loop!")
        print("")

# end the while loop if user input = -1
else:
    # check values
    if len(my_list) == 0:
        # ouput if nothing is stored - i.e. -1 is entered first
        print("Nothing has been stored!")
    elif sum(my_list) == 0:
        # output if sum of values is 0
        print("The sum of all values is 0! The average has to be 0!")
    else:
        # otherwise calculate and output the average of all values in list
        print(
            f"The average of the stored numbers is {str(sum(my_list)/len(my_list))}")
