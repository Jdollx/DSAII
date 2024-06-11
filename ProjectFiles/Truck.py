# creat Truck class
class Truck:

    # constructor for truck object
    def __init__(self, truck_number, package_limit, speed, load, packages, miles, truck_address, departure_time, time_of_day):
        self.truck_number = truck_number
        self.package_limit = package_limit
        self.speed = speed
        self.load = load
        self.packages = packages
        self.miles = miles
        self.truck_address = truck_address
        # this is the time of day
        self.departure_time = departure_time
        # this is the time the truck leaves in the morning
        self.time_of_day = time_of_day

    # method to format to string
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (
            self.truck_number,
            self.package_limit,
            self.speed,
            self.load,
            self.packages,
            self.miles,
            self.truck_address,
            self.departure_time,
            self.time_of_day
        )
