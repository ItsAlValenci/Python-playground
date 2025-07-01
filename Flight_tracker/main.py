import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
json_data = data_manager.get_destination_data()
print("Data loaded successfully.\n")

flight_search = FlightSearch()

# Initialize notification manager for sending alerts
notification_manager = NotificationManager()
print("Notification manager initialized.\n")

# Setting City of Origin (IATA CODE)

ORIGIN_CITY_IATA = "SFO"

# ==================== Update the Airport Codes Json ====================
# Check if any city needs an IATA code
empty_codes_exist = False
for place in json_data["Albert"]:
    if place["iataCode"] == "":
        empty_codes_exist = True
        break

# If empty codes exist, create flight search and update all cities
if empty_codes_exist:
    flight_search = FlightSearch()
    for place in json_data["Albert"]:
        place["iataCode"] = flight_search.get_destination_code(place["city"])
    print("IATA code updated\n")
    
    # Update the data manager and save changes
    data_manager.destination_data = json_data
    data_manager.update_destination_code()
else:
    print("Every city has an IATA code.\n")

# ==================== Search for Flights ====================

# we want to search for the following 6 months.
departure_date = datetime.now() + timedelta(days=30)
return_date = departure_date + timedelta(days=(7*3))

for destination in json_data["Albert"]:
    print(f"Getting rates for {ORIGIN_CITY_IATA} to {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=departure_date,
        to_time=return_date
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price} from {cheapest_flight.carrier}\n")
    
    # Send notification to Discord if a valid flight was found
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["LowestPrice"]:
        notification_manager.send_flight_deal_notification(
            flight_data=cheapest_flight,
            city=destination['city']
        )
        print(f"Discord notification sent for {destination['city']}")
    
    # Slowing down requests to avoid rate limit
    time.sleep(2)
