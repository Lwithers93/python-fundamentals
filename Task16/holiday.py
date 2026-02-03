cities = {
    "Tokyo": {
        "hotel": "£200",
        "flight": "£700",
        "rental": "£40"
    },
    "Capetown": {
        "hotel": "£150",
        "flight": "£800",
        "rental": "£60"
    },
    "Sydney": {
        "hotel": "£250",
        "flight": "£1000",
        "rental": "£40"
    },
    "Auckland": {
        "hotel": "£300",
        "flight": "£1200",
        "rental": "£35"
    }}

holiday_city = ""


def validate_input(inp):
    # Create validation function for later use
    while True:
        try:
            val = int(inp)
        except ValueError:
            inp = input(
                "Invalid Input. Please enter a whole number. ")
        else:
            break
    return inp


print("\nLet's calculate your holiday cost!")

print("\nFirst, choose a destination!")
print("\nDestination choices: ")
for city, info in cities.items():
    print(f"{city} from {info['hotel']} per night\n")

# Get all user inputs

# Get city flight user input
holiday_city = input("Which city would you like to visit? ").capitalize()
# Validate input
while holiday_city not in cities:
    print(holiday_city)
    holiday_city = input(
        "Please choose one of the above cities! ").capitalize()
# Get number of nights user input
num_of_nights = input("How many nights will you be staying? ")
# Validate input
num_of_nights = int(validate_input(num_of_nights))
# Get rental days user input
rental_days = input("How many days will you rent a car for? ")
# Validate input
rental_days = int(validate_input(rental_days))

# Define functions


def hotel_cost(city, nights):
    # Define hotel cost function
    price = int(cities.get(city).get('hotel')[1:])
    cost = price * nights
    return cost


def plane_cost(city):
    # Define plane cost function
    price = int(cities.get(city).get('flight')[1:])
    return price


def rental_car_cost(city, rental):
    # Define car rental function for car rental cost
    price = int(cities.get(city).get('rental')[1:])
    cost = price * rental
    return cost


def total_holiday_cost(city, nights, rental):
    # Define holiday cost function for total cost of holiday
    total = hotel_cost(city, nights) + plane_cost(city) + \
        rental_car_cost(city, rental)
    return total


print("\nHere is the cost breakdown for your holiday: ")

# Output the hotel cost
print(
    f"\nThe hotel will cost you £{hotel_cost(holiday_city, num_of_nights)} in total.\n")

# Output the plane flight cost
print(
    f"The flights will cost you £{plane_cost(holiday_city)}.\n")

# Output the rental car cost
print(
    f"The rental car will cost you £{rental_car_cost(holiday_city,rental_days)} for the trip.\n")

# Output the total cost of the trip
print(
    f"The holiday will cost you £{total_holiday_cost(holiday_city,num_of_nights, rental_days)} in total.\n")
