## Task 11 Practical Task 1

# get a string from the user and print it back to them
print("")
user_input = str(input("Please enter a sentence: "))
print("")
print(f"Thank you. Your sentence is: {user_input}")
print("")

# STEP 1
# make each alternate CHARACTER an upper case char and all others lower case characters
print(
    "For step 1, we will change your sentence so each character alternates between upper and lower case."
)
print("")

# initialise the string variable to store the new string
new_string1 = ""

# loop through the given string
for x, char in enumerate(user_input):
    # if the index is even, make the char upper case
    if x % 2 == 0:
        new_string1 += char.upper()
    # otherwise (i.e. if odd), make the char lower case
    else:
        new_string1 += char.lower()

# print the result
print(f"Your new alternating upper and lower case string is: {new_string1}")
print("")

# STEP 2
# now make each alternate WORD of the same string lower or upper case
print(
    "For step 2, we will change your sentence so each word alternates between upper and lower case."
)
print("")

# split the given string into a list of words
words_list = user_input.split()

# show the new list // used for debug
# print(f"The new words list is: {words_list}")
# print("")

# initialise result list
result_list = []

# loop through the given array
for x, word in enumerate(words_list):
    # if the index is even, make the word in the array upper case
    if x % 2 == 0:
        result_list.append(word.upper())
    # otherwise (i.e. if odd), make the word in the array lower case
    else:
        result_list.append(word.lower())

# show the rough result of the loop // used for debug
# print(f"The new list after the loop is: {result_list}")
# print("")

# make the result list into new string variable using join()
new_string2 = " ".join(result_list)

# print new string variable with alternating words in upper and lower case
print(f"Your new string with alternating upper and lower case words is: {new_string2}")
