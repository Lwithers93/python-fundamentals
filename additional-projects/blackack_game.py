import random

# declare variables for making deck
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
deck = []

# declare other game variables for later use
player_cards = []
player_total = 0
player_hand = ""
dealer_cards = []
dealer_total = 0
dealer_hand = ""


### DEFINING FUNCTIONS ###


# define deck making function
def make_deck():
    for a in range(number_of_decks):
        for x in suits:
            for y in values:
                if y in ["King", "Queen", "Jack"]:
                    p = 10
                elif y == "Ace":
                    p = 11
                else:
                    p = int(y)
                new_card = {
                    "suit": x,
                    "value": y,
                    "points": p,
                }
                deck.append(new_card)


# define deal function
def deal():
    for x in range(2):
        # declare variables are global
        global player_hand
        global player_total
        # choose player card from deck
        card_one = random.choice(deck)
        # remove card from deck
        deck.remove(card_one)
        # add card to players hand
        player_cards.append(card_one)

        # choose dealer card
        card_two = random.choice(deck)
        # remove card from main deck
        deck.remove(card_two)
        # add card to dealer hand
        dealer_cards.append(card_two)

        # add player hand variable for print output
        player_hand += f"{player_cards[x]['value']} of {player_cards[x]['suit']}, "
        # add player points to points variable (points i.e. the value of each card)
        player_total += int(player_cards[x]["points"])

    # output the player's current hand and points
    print(f"player has: {player_hand}. Player is on {player_total} points.")
    print("")

    # output the dealer's first card and points (2nd card is always hidden until after user's turn complete)
    print(
        f"dealer has: {dealer_cards[0]['value']} of {dealer_cards[0]['suit']}. Dealer is on {dealer_cards[0]['points']} points."
    )


### RUNNING THE GAME ###

# user to input number of decks for game (e.g. 1,2,3 etc)
number_of_decks = int(input("How many decks? "))

# call deck making function
make_deck()

# call deal function
deal()
