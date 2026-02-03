# Open the relevant file
file = open("DOB.txt", "r+", encoding="utf-8")
# Declare two list variables for later use
name_list = []
dob_list = []

# Loop through the file by each line
for line in file:
    # Convert each line into a string list
    string_list = line.split()
    # Take the relevant name values from the list
    full_name = f"{string_list[0]} {string_list[1]}"
    # Add name values to full_name_list
    name_list.append(full_name)
    # Repate the above but adding dob to dob_list
    dob = f"{string_list[2]} {string_list[3]} {string_list[4]}"
    dob_list.append(dob)

# Print a bold 'Name' statement followed by name_list
print("\033[1mName\033[0m")
for name in name_list:
    print(name)

# Print a bold 'Birthdate' statement followed by dob_list
print("\n\033[1mBirthdate\033[0m")
for dob in dob_list:
    print(dob)

# Close file when complete
file.close()
