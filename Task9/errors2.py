# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"  # syntax error: missing "" for string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  # logical error: missing 'f' for f string
# logical error: incorrect variable order (switched number_of_teeth and animal_type)

print(full_spec)  # syntax error: missing parentheses
