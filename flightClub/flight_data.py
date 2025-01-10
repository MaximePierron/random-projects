from datetime import datetime


flights_info = []


def clean_flight_data(flights):
    for flight in flights:

        city_from = flight["cityFrom"]
        fly_from = flight["flyFrom"]
        city_to = flight["cityTo"]
        fly_to = flight["flyTo"]
        dateFrom = datetime.strptime(flight["route"][0]["local_departure"], "%Y-%m-%dT%H:%M:%S.%fZ")
        dateTo = datetime.strptime(flight["route"][-1]["local_arrival"], "%Y-%m-%dT%H:%M:%S.%fZ")
        price = flight["price"]
        airline = flight["route"][0]["airline"]
        link = flight["deep_link"]

        flight_info = {
            "fly_from": f"{city_from}-{fly_from}",
            "fly_to": f"{city_to}-{fly_to}",
            "dateFrom": dateFrom,
            "dateTo": dateTo,
            "price": price,
            "airline": airline,
            "link": link
        }

        if len(flight["route"]) > 4:
            stop_over_city = flight["route"][0]["cityTo"]
            stop_over_airport = flight["route"][0]["flyTo"]
            flight_info["stop_over"] = f"{stop_over_city}-{stop_over_airport}"
        else:
            flight_info["stop_over"] = "None"

        flights_info.append(flight_info)
    return flights_info
