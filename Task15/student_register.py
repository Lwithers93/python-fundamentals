# Create validation function for later use
def validate_input(inp):
    while True:
        try:
            val = int(inp)
        except ValueError:
            inp = input(
                "Invalid Input. Please enter a whole number. ")
        else:
            break
    return inp

# Begin program


print("Welcome to the registration hub!")
# Get many students are registering
number_of_students = input("How many students are registering? ")
number_of_students = validate_input(number_of_students)
print("Thank you")

# Open file ready for loop
file = open("reg_form.txt", "w")
file.write("Student ID     Signature")

# Get int value for loop
number_of_students = int(number_of_students)

# Loop thrrough x number of students
for student in range(number_of_students):
    # Get ID number for each student
    student_ID = input("Please enter the 7 digit student ID: ")
    student_ID = validate_input(student_ID)
    while len(student_ID) != 7:
        student_ID = input(
            "Error - ID Must be 7 digits. Please re-enter the 7 digit student ID: ")
        student_ID = validate_input(student_ID)
    print("Thank you. Student ID accepted.")

    # Write Student ID to reg form file

    file.write(f"\n{student_ID}")
    # Include dotted line after each student
    file.write("        .........................")

# Close file when complete
file.close()
