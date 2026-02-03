# pseudo code

# welcome user to calculator
# declare 3 variables for swim, bike, run based on user input
# calculate total time based on 3 variables
# if the total time is 111+ mins, print "No award"
# if total time is 106-110 mins, print "Provincial Stroll"
# if time is 101-105 mins, print "Half colours"
# if time is 0-100 mins, print "Provincial Colours"

# code

# congratulate user for completing triathlon
print(
    "Conrgratulations on completing your triathlon! Everyone here today is a winner!"
)
# print empty line space
print("")
# welcome user to calculator.
print(
    "We will now calculate if you have qualified for an award!"
)

# declare variables for each event by user input
swim = int(
    input(
        "How long did your swimming section take (in minutes)? "
    )
)
bike = int(
    input(
        "How long did your cycling section take (in minutes)? "
    )
)
run = int(
    input(
        "How long did your running section take (in minutes)? "
    )
)
# declare variable to hold string statement for award output use
congrats = "Congratulations! You have received the"

total_time = swim + bike + run

if total_time >= 111:
    # output if greater than or equal to 111 minutes total time
    print(
        "Unfortunately, your time was not fast enought to receive an award. Better luck next time!"
    )
elif total_time >= 106:
    # output relevant award and text with f string
    print(
        f"{congrats} Provincial Stroll Award!")
elif total_time >= 101:
    # output relevant award and text with f string
    print(
        f"{congrats} Provincial Half Colours Award!"
    )
else:
    # output relevant award and text with f string
    print(
        f"{congrats} Provincial Colours Award!"
    )
