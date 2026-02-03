# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print(
    "Welcome to the error program"
)  # Syntax error: missing parentheses around print string
print(
    "\n"
)  # Syntax error: missing parentheses around print string and incorrect indentation

# Variables declaring the user's age, casting the str to an int, and printing the result

age_str = "24 years old"  # Syntax error: incorect variable naming convention and assignment operator "==" should be "="
#  Corrected to snake case. Also removed incorrect indentation

age = 24  # runtime error: cannot convert string "years old" to int. changed variable declaration.
# additional syntax error: incorect variable naming convention (age_Str should be age_str). Corrected to snake case.
# Also incorrect indentation

print(
    f"I'm {age} years old."
)  # Syntax error: incorrect indentation. added f string to allow for easier concatenation

# Variables declaring additional years and printing the total years of age

years_from_now = "3"  # syntax: incorrect indentation.
total_years = age + int(years_from_now)  # syntax: incorrect indentation.
# runtime error: years_from_now must be integer. Used int() function, but could also change previous
# declaration to integer instead of string

print(
    f"The total number of years: {total_years}"
)  # Syntax error: missing parentheses around print string
# Syntax error: variable written incorrectlt and as string. Corrected with f string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (
    total_years * 12
)  # syntax error: incorrect variable name, should be total_years
print(
    "In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old"
)  # syntax error: missing parentheses.
# logical error: added + 6 to variable to account for additional 6 months not included in total_months variable
# runtime error: added str() function to variable as cannot concatenate integer to str

# HINT, 330 months is the correct answer
