import data_manager
import flight_data
import flight_search
import pandas as pd
import notification_manager

price_data = data_manager.get_prices()
user_data = data_manager.get_users()
cheap_flights = []

for price in price_data:
    city = price["city"]
    city_id = price["id"]
    city_code = flight_search.get_iata_code(city)
    data_manager.put_iata_code(city_id, city_code)

for price in price_data:
    city_code = price["iataCode"]
    threshold_price = price["lowestPrice"]
    flights = flight_data.clean_flight_data(flight_search.search_for_flights(city_code))
    for flight in flights:
        if flight["price"] <= threshold_price:
            cheap_flights.append(flight)

# Between these two blocks, cheap-flights somehow gets flights above threshold.
cheapest_flights_list = []

if len(cheap_flights) > 0:
    df = pd.DataFrame(cheap_flights)
    for destination in df["fly_to"].unique():
        partial_df = df[df.fly_to == destination].sort_values(by="price")
        cheapest_flights_list.append(partial_df.iloc[:1].to_dict('records')[0])

for user in user_data:
    first_name = user["firstName"]
    email = user["email"]

    mail_content = f"Hey {first_name}! Here are a few great deals for your next holidays:\n\n"

    for cheapest_flight in cheapest_flights_list:
        fly_from = cheapest_flight["fly_from"]
        fly_to = cheapest_flight["fly_to"]
        date_from = cheapest_flight["dateFrom"]
        date_to = cheapest_flight["dateTo"]
        price = cheapest_flight["price"]
        airline = cheapest_flight["airline"]
        stop_over = cheapest_flight["stop_over"]
        link = cheapest_flight["link"]
        flight_message = f"From {fly_from} to {fly_to}, from {date_from} to {date_to}, for {price} € with {airline}.\n"
        if stop_over != "None":
            flight_message += f"One stop over in {stop_over}.\n"
        flight_message += f"Go to:\n{link}\n\n"
        mail_content += flight_message
    notification_manager.send_flights_email(email, mail_content)



