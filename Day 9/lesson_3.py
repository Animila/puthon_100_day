travel_log = [
    {
        "country": "France",
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
    {
        "country": "Germany",
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


def add_new_country(country, total, cities):
    new_country = {}
    travel_log.append(new_country)
    numbers = travel_log.index(new_country)

    travel_log[numbers]["country"] = country
    travel_log[numbers]["total_visits"] = total
    travel_log[numbers]["cities_visited"] = cities

    travel_log.remove(travel_log[numbers])

    new_country = {}
    new_country["country"] = country
    new_country["total_visits"] = total
    new_country["cities_visited"] = cities
    travel_log.append(new_country)



add_new_country("Russian", 2, ["Moscow", "Saint Peterburg"])
print(travel_log[0])
print(travel_log[1])
print(travel_log[2])
print(travel_log[3])
