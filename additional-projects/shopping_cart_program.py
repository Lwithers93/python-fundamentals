### DECLARE VARIABLES ###

# dash variable used to output a line of "-" string
dash = "-" * 79

# user starting "gold"/money
user_gold = 200
# user bag contents
user_bag = ["potion", "pokeball", "bike"]
# list of items selected at the mart
item_pick_list = []

# the items available at the mart
mart_items = [
    {
        "name": "potion",
        "price": "200",
    },
    {
        "name": "pokeball",
        "price": "300",
    },
    {
        "name": "antidote",
        "price": "100",
    },
]

# names of mart_items
mart_item_names = []
# get the mart item names and populate variable
for x in mart_items:
    mart_item_names.append(x["name"])


### DEFINING FUNCTIONS ###


# define a function to check input is valid
def check_input(inp, var):
    while inp not in (var):
        print("Invalid choice.")
        inp = input(f"Please enter a choice from: {var} > ").lower()
    return inp


# define a function to find a dictionary item based on key and value
def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


### RUNNING THE PROGRAM ###


print(dash)
print("Hello, How may I help you?")
print("")
print("Buy | Sell")
print("")

# get user input to choose buy or sell
user_input = input("Please enter 'Buy' or 'Sell' > ").lower()
# check input is valid
user_input = check_input(user_input, ["buy", "sell"])

# if buy is selected, show user the items in stock
if user_input == "buy":
    print(dash)
    print("Here's what we have in stock: ")
    print(dash)

    # loop through to print each item
    for item in mart_items:
        print(f"{item['name']}: {item['price']}")

    print(dash)
    # get user input to see if they want anything
    choose_item = input("See anything you like? > ").lower()
    # check input is valid
    choose_item = check_input(choose_item, ["y", "n"])

    # if input is "Y", ask user which item
    if choose_item == "y":
        print("")
        # get user input with item name
        item_pick = input("which item would you like? > ").lower()
        # check input is valid
        item_pick = check_input(item_pick, mart_item_names)

        # while the user keeps selecting items, continue to loop
        while item_pick in (mart_item_names):
            # find the selected item and check it's cost
            index = find(mart_items, "name", item_pick)
            cost = int(mart_items[index]["price"])

            # if cost is less than or equal to gold, then buy
            if cost <= user_gold:
                # add to pick list
                item_pick_list.append(item_pick)
                # subtract amount from user gold
                user_gold = user_gold - cost
                # print to confirm purchase
                print(f"You bought the {item_pick}!")
            else:
                # if cost is more than gold, tell user they can't afford
                print("You don't have enough money for that!")

            print("")
            # get user input for another choice
            another_pick = input("Would you like something else? > ").lower()
            # confirm if input is valid
            another_pick = check_input(another_pick, ["y", "n"])
            # if user wants another item, ask again
            if another_pick == "y":
                print("")
                # get user input
                item_pick = input("What would you like? > ").lower()
                # check input valid
                item_pick = check_input(item_pick, mart_item_names)
            else:
                # if no more items desired, end loop
                break
        print("")
        # after loop say thank you
        print("Thank you for stopping by!")
        print("")
        # print picked list of items
        print(f"Here are the items you've purchased today:\n{''.join(item_pick_list)}")

        # run through list and add all items to user bag
        for x in item_pick_list:
            user_bag.append(x)

        print("")
        # show user updated bag content
        print(f"In your bag you now have: ")
        print("\n".join(user_bag))

    # if input is "N" (after seeing items available), ask user if they want to sell instead
    else:
        print("")
        # get user input if they would like to sell instead
        next_input = input("Would you like to sell something instead? > ")
        # check input is valid
        next_input = check_input(next_input, ["y", "n"])

        # if "no", say thanks and exit
        if next_input == "n":
            print("Thank you for stopping by!")

        # else show the selling options
        else:
            print("Here are the options for selling...")

# Buy not selected means Sell selected. Show Sell options to user
else:
    print("Here are the options for selling...")
