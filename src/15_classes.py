# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

#testing with print example
test = LatLon(5, 10)
print(test.lat, test.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon): 
        self.name = name   
        super().__init__(lat, lon)

    def __str__(self):
        print(f'name: {self.name}, lat: {self.lat}, lon: {self.lon}')

#testing with print example
test = Waypoint("City", 5, 10)
print(test.name, test.lat, test.lon, test.name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint): 
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        print(f'name: {self.name}, difficulty: {self.difficulty}, size: {self.size}, lat: {self.lat}, lon: {self.lon}')


#testing with print example
test = Geocache("City", "easy", "large", 5, 10)
print(test.name, test.difficulty, test.size, test.lat, test.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.name, waypoint.lat, waypoint.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache.name, geocache.difficulty, geocache.size, geocache.lat, geocache.lon)

# Print it--also make this print more nicely
print(geocache)
