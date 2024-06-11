import datetime

# create Package class
class Package:

    # constructor for package object
    def __init__(self, package_id, package_address, city, state, zip_code, delivery_deadline, weight_kilo, delivery_status, truck_number):
        self.package_id = package_id
        self.package_address = package_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight_kilo = weight_kilo
        self.delivery_status = delivery_status
        self.departure_time = None # referenced later to document @ time package departed
        self.delivery_time = None # referenced later for document @ time package delivered
        self.truck_number = truck_number

    # method to format to string
    def __str__(self):
        # checks if delivery time is None
        delivery_time_str = str(self.delivery_time) if self.delivery_time is not None else "Not delivered"
        return "Package ID: {}, Address: {} {} {} {}, Deadline: {}, Weight: {}, " \
               "Delivery Time: {}, Status: {}, Truck: {}".format(
            self.package_id,
            self.package_address,
            self.city,
            self.state,
            self.zip_code,
            self.delivery_deadline,
            self.weight_kilo,
            delivery_time_str,
            self.delivery_status,
            self.truck_number
        )

    # update address method for package 9
    def update_package_9(self, time_of_day):

        # checks if package ID is 0 and the time is equal to or later than 10:20
        if self.package_id == 9 and time_of_day >= datetime.timedelta(hours=10, minutes=20):
            # update package address information
            self.package_address = "410 S State St"
            self.city = "Salt Lake City"
            self.state = "UT"
            self.zip_code = "84111"
        # defaults to old address
        else:
            self.package_address = "300 State St"
            self.city = "Salt Lake City"
            self.state = "UT"
            self.zip_code = "84103"

    # method to update delivery status
    def update_status(self, time_of_day):

        # checks if the delivery time is before the inputted time
        if self.delivery_time < time_of_day:
            self.delivery_status = "Delivered"

        # checks if departure time is later than or equal to the inputted time
        elif self.departure_time > time_of_day:
            self.delivery_status = "At hub"

        # defaults
        else:
            self.delivery_status = "En route"