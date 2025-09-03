def hotel_cost(nights):
    return 140 * nights #$140 per night

def car_rental(days, city):
    if city == " LA ":
        return 55 * days
    elif city == " Chicago ":
        return 50 * days
    elif city == " NY ":
        return 45 * days
    else:
        return 55 * days #default cost

def flight_cost(city):
    if city ==  " LA ":
        return 250
    elif city == " Chicago ":
        return 200
    elif city == " NY ":
            return 180
    else:
        return 400 #default cost
        
def trip_cost(city, days, spending_money): 
    hotel = hotel_cost(days)
    car = car_rental(days,city)
    flight = flight_cost(city)
    total = hotel + car + flight + spending_money
    
    print("----- Vacation Planner -----")
    print("Destination:", city)
    print("Hotel cost: $", hotel)
    print("Days:", days)
    print("Car rental cost: $", car)
    print("Flight cost: $", flight)
    print("Spending money: $", spending_money)
    
    #value edits
    
    city_choice = "Seattle"
    days = 5
    spending_money = 800
    
    #----------
    
    #call fuction
    
trip_cost(city_choice, days, spending_money)
    
    
        