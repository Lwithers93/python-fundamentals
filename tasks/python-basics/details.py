# Practical task two

## Pseudo code

# Get user name from user input
# Get user age from input
# Get user house number from input
# Get user street name from input
# Print single statement with user info

## Code

# Request username as input
user_name = input("Please enter your name: ")

# Request user age as input, do not cast to integer as used in string later
user_age = input("Please enter your age: ")

# Request house number, do not cast number to integer in case house number includes letter e.g. "5C"
user_house_num = input("Please enter your flat/house number: ")

# Request user street name
user_street_name = input("Please enter your street name: ")

# Print output with concatenated user details. f string used to assist in concatenation.
print(
    f"This is {user_name}. He is {user_age} years old and lives at number {user_house_num} on {user_street_name}"
)
