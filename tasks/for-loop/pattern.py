# Practical Task One

# pseudo code
# create list variable to add * to
# loop through list 5 times adding and printing one "*" each loop
# once loop is past 5 occurences, continue to loop but remove one "*"

# code

# declare empty list variable
display_list = []

# start loop
for x in range(9):
    # for first 5 occurrences, add an "*" and print list
    if x < 5:
        display_list.append("*")
        print(*display_list, sep="")
    # for last 4 occurrences, remove "*" and print list
    else:
        display_list.pop()
        print(*display_list, sep="")
