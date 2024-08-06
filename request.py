import json
from typing import Dict
from common import City, Location, Flight, Housing, TransportationMethod, Journey

def initialize_classes_from_json(json_path: str):
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Create City instances
    cities = {city['name']: City(name=city['name'], priority=city['priority']) for city in data['cities']}

    # Create Location instances
    locations = {city['name']: Location(latitud=city['location']['latitud'], longitud=city['location']['longitud'], city=cities[city['name']]) for city in data['cities']}

    # Create Flight instances
    flights_from_madrid = []
    flights_to_madrid = []

    for flight in data['flights']:
        flight_instance = Flight(
            origin=locations[flight['origin']],
            destination=locations[flight['destination']],
            prize=flight['prize'],
            scales=flight['scales'],
            time_spent=flight['time_spent']
        )
        if flight['origin'] == 'Madrid':
            flights_from_madrid.append(flight_instance)
        elif flight['destination'] == 'Madrid':
            flights_to_madrid.append(flight_instance)

    # Create Housing instances
    housing = [
        Housing(
            location=next(loc for loc in locations.values() if loc.latitud == house['location']['latitud'] and loc.longitud == house['location']['longitud']),
            prize_night=house['prize_night'],
            num_nights=house['num_nights'],
            rating=house['rating'],
            capacity=house['capacity'],
            distance_to_center=house['distance_to_center']
        )
        for house in data['housing']
    ]

    # Create TransportationMethod instances
    transportation_methods = [
        TransportationMethod(
            origin=locations[transport['origin']],
            destination=locations[transport['destination']],
            transport_method=transport['transport_method'],
            prize=transport['prize'],
            scales=transport['scales'],
            time_spent=transport['time_spent']
        )
        for transport in data['transportation_methods']
    ]

    journey = Journey(
        visited_cities=list(cities.values()),
        duration=10,
        transport=transportation_methods,
        housing=housing,
        flights=(flights_from_madrid, flights_to_madrid)  # Separate flights from Madrid and to Madrid
    )

    return journey

journey = initialize_classes_from_json('data.json')
