# Practical task 1

# Create a list with four items sold in the cafe
menu = ["burger", "fries", "milkshake", "coffee"]

# Create a dictionary called 'stock' that contains the stock value per menu items
stock = {
    "burger": 10,
    "fries": 50,
    "milkshake": 15,
    "coffee": 100,
}

# Create a dictionary called 'price' that contains the price value for each menu items
# Price values could be stored as float values but string used instead to allow "£"
price = {
    "burger": "£8.00",
    "fries": "£3.00",
    "milkshake": "£3.50",
    "coffee": "£2.50",
}

# Declare an empty variable for stock worth
total_stock_worth = 0
# Begin loop through menu items
for item in menu:
    # Remove the "£" and convert to float from string
    price_as_float = float(price[item][1::])
    # Multiply the number of each item in stock by the newly generated float value for price
    total_stock_worth += stock[item] * price_as_float

# Print output of the loop ensuring two decimal places for price readability
print(f"The total value of the items in stock is: £{float(total_stock_worth):.2f}")
