# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# https://beginnersbook.com/2018/03/python-constructors-default-and-parameterized/
# https://www.erol.si/2016/01/python-and-multiple-constructors/
# YOUR CODE HERE
# Have to MAKE SURE you use __init__ and not _init_ or it won't work. Same with __str__ vs _str_


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# https://www.pythonforbeginners.com/super/working-python-super-function
# https://appdividend.com/2019/01/22/python-super-function-example-super-method-tutorial/
# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return (f"Waypoint '{self.name}' {self.lat} {self.lon}")
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return (f"Geocache '{self.name}' {self.difficulty} {self.size} {self.lat} {self.lon}")
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)
