# Vacation Planner

# --- Functions ---
def hotel_cost(nights):
    return nights * 100

def car_rental(days, car_type):
    if car_type.lower() == "economy":
        return days * 40
    elif car_type.lower() == "suv":
        return days * 60
    else:
        return days * 50  # default

def flight_cost(city):
    if city.lower() == "new york":
        return 300
    elif city.lower() == "los angeles":
        return 350
    elif city.lower() == "chicago":
        return 280
    else:
        return 400  # default

def trip_cost(city, nights, days, car_type):
    return hotel_cost(nights) + car_rental(days, car_type) + flight_cost(city)


# --- Main program ---
print("Welcome to the Vacation Planner!")

# Ask for inputs first
city_choice = input("Enter your destination city (New York, Los Angeles, Chicago): ")
nights = int(input("How many nights will you stay? "))
days = int(input("How many days will you rent a car? "))
car_type = input("What type of car would you like (Economy, SUV, Other)? ")

# Calculate total
total = trip_cost(city_choice, nights, days, car_type)

# Show result
print("\n--- Vacation Summary ---")
print(f"Destination: {city_choice}")
print(f"Hotel cost: ${hotel_cost(nights)}")
print(f"Car rental ({car_type}): ${car_rental(days, car_type)}")
print(f"Flight to {city_choice}: ${flight_cost(city_choice)}")
print(f"Total trip cost: ${total}")
