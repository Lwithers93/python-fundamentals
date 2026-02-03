# Practical Task one

## pseudo code
# get the user age and store in a variable called age
# if the user age is over 100, output "Sorry, you're dead"
# if the user is 65 or older, "Enjoy your retirement"
# if the user is over 40, say "You're over the hill."
# if the user is 21, output "Congrats on your 21st"
# if under 13 output "You qualify for the kiddie discount"
# for ANY other age, output "Age is but a number"

## code

# gets user age as input
user_age = int(input("Please enter your age: "))

# checks if user age is over 100
if user_age > 100:
    print("Sorry... You're dead.")
# checks if user age is over or equal to 65
elif user_age >= 65:
    print("Enjoy your retirement!")
# checks if user age over 40
elif user_age > 40:
    print("You're over the hill!")
# checks if user age is 21
elif user_age == 21:
    print("Congrats on your 21st!")
# checks if user is under 13
elif user_age < 13:
    print("You qualify for the kiddie discount!")
# return output for any other age
else:
    print("Age is but a number!")
