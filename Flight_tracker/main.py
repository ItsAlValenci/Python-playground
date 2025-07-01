import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

data_manager = DataManager()
json_data = data_manager.get_destination_data()
print("Data loaded successfully.\n")

flight_search = FlightSearch()

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
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in json_data["Albert"]:
    print(f"Getting rates for {ORIGIN_CITY_IATA} to {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
