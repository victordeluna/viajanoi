from typing import List, Tuple

# Classes

class City:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority

class Location:
    def __init__(self, latitud: float, longitud: float, city: City):
        self.latitud = latitud
        self.longitud = longitud
        self.city = city

class Flight:
    def __init__(self, origin: Location, destination: Location, prize: float, scales: bool, time_spent: int):
        self.origin = origin
        self.destination = destination
        self.prize = prize
        self.scales = scales
        self.time_spent = time_spent

class Housing:
    def __init__(self, location: Location, prize_night: float, num_nights: int, rating: float, capacity: int, distance_to_center: int):
        self.location = location
        self.prize_night = prize_night
        self.num_nights = num_nights
        self.rating = rating
        self.capacity = capacity
        self.distance_to_center = distance_to_center
    
    def cost_per_housing(self):
        return self.prize_night * self.num_nights

class TransportationMethod:
    def __init__(self, origin: Location, destination: Location, transport_method: str, prize: float, scales: bool, time_spent: int):
        self.origin = origin
        self.destination = destination
        self.transport_method = transport_method
        self.prize = prize
        self.scales = scales
        self.time_spent = time_spent

class Journey:
    def __init__(self, visited_cities: List[City], duration: int, transport: List[TransportationMethod], housing: List[Housing], flights: Tuple[Flight, Flight]):
        self.visited_cities = visited_cities
        self.duration = duration
        self.transport = transport
        self.housing = housing
        self.flights = flights
    
    def total_transport_time(self):
        return sum(trans.time_spent for trans in self.transport) + sum(fli.time_spent for fli in self.flights)
    
    def total_transport_cost(self):
        return sum(trans.prize for trans in self.transport)
    
    def total_housing_cost(self):
        return sum(house.cost_per_housing() for house in self.housing)
    
    def total_flight_cost(self):
        return sum(fli.prize for fli in self.flights)
    
    def total_cost(self):
        return self.total_housing_cost() + self.total_transport_cost() + self.total_flight_cost()
