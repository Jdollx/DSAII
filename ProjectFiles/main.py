# Student ID: 011783233
# Author: Jennifer Doll
# Title: JenniferDollDSAII
# Date: March 7, 2024

import csv
import datetime

from Truck import Truck
from Package import Package
from ProjectFiles.CreateHashTable import CreateHashTable

# reads Distance CSV file
with open("ProjectFiles/WGUPSDistanceTableCSV.csv", 'r') as csvfile_dist:
    CSVDistance = csv.reader(csvfile_dist)
    CSVDistance = list(CSVDistance)

# reads Address CSV file
with open("ProjectFiles/WGUPSAddressTableCSV.csv", 'r') as csvfile_address:
    CSVAddressTable = csv.reader(csvfile_address)
    CSVAddressTable = list(CSVAddressTable)

# reads Package CSV file
with open("ProjectFiles/WGUPSPackageFileCSV.csv", 'r') as csvfile_package:
    CSVPackage = csv.reader(csvfile_package)
    CSVPackage = list(CSVPackage)

# gets distance between addresses
def get_distance(x_dist, y_dist):

    # if first parameter > second parameter input
    if x_dist > y_dist:
        # returns float (x,y)
        return float(CSVDistance[x_dist][y_dist])
    else:
        # returns float (y,x) to account for inversion of graph
        return float(CSVDistance[y_dist][x_dist])

# gets address from csv
def get_address(address):

    # iterates through rows in csv
    for row in CSVAddressTable:
        # checks to see if inputted address in row
        if address in row[2]:
            # returns the index of that address
            return int(row[0])
    return None

# loads package info/creates package object
# SOURCE: C950 - Webinar-2 - Getting Greedy, who moved my data?
def load_package_info():

    # iterates through rows in csv
    for row in CSVPackage:
        # extract data from each row
        package_id = int(row[0])
        package_address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        delivery_deadline = row[5]
        weight_kilo = row[6]
        # default status
        delivery_status = "At hub"
        # default number
        truck_number = None

        # create package object
        package_object = Package(package_id, package_address, city, state, zip_code, delivery_deadline, weight_kilo, delivery_status, truck_number)
        # add package into hashtable by ID
        package_hash_table.insert(package_id, package_object)

# hash table instance
package_hash_table = CreateHashTable()

# call Package file
load_package_info()

# constants - (package_limit=16packages, speed=18, load=None, miles=0.0, address=4001 South 700 East)
# create truck 1 object - 8:00 start time
Truck_1 = Truck(1, 16, 18, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours = 8, minutes = 0), datetime.timedelta(hours = 8, minutes = 0))

# create truck 2 object - 10:20 start time
Truck_2 = Truck(2, 16, 18, None, [3, 5, 7, 8, 9, 11, 12, 17, 18, 21, 24, 25, 36, 38], 0.0, "4001 South 700 East", datetime.timedelta(hours = 10, minutes = 20), datetime.timedelta(hours = 10, minutes = 20))

# create truck 3 object - 9:33 start time after truck 1 gets back
Truck_3 = Truck(3, 16, 18, None, [2, 4, 6, 10, 22, 23, 25, 26, 27, 28, 32, 33, 35], 0.0, "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 33), datetime.timedelta(hours = 9, minutes = 33))

# # prints out hash table
# for i in range(len(package_hash_table.table) + 1):
#     print("Index: {} {}".format(i, package_hash_table.search(i+1)))

# nearest neighbor algorithm to deliver packages
# SOURCE: C950 WGUPS Project Implementation Steps - Example - Nearest Neighbor - https://srm--c.vf.force.com/apex/CourseArticle?id=kA03x000001DbBGCA0&groupId=&searchTerm=&courseCode=C950&rtn=/apex/CommonsExpandedSearch
# SOURCE: Approximate solutions: nearest neighbor algorithm - https://www2.seas.gwu.edu/~simhaweb/champalg/tsp/tsp.html
def deliver_packages(truck):

    # empty list for undelivered packages
    undelivered_packages = []

    # iterate through package IDs in list of packages assigned to a truck - loading packages onto the truck
    for package_id in truck.packages:
        # use package ID to lookup method the package information in the hash table
        package = package_hash_table.lookup(package_id)
        # add package information to list of undelivered packages
        undelivered_packages.append(package)

    # remove all packages from truck
    truck.packages.clear()

    # loop while there are packages in undelivered list
    while len(undelivered_packages) > 0:
        # set next neighbor distance to infinity
        next_neighbor_distance = float('inf')
        # set next neighbor package to none
        next_neighbor_package = None

        # iterate through undelivered packages for next closest neighbor package
        # this for loop iterates through the packages and determines the shortest distance to the next package
        for package in undelivered_packages:

            # distance between the truck and the current package
            distance = get_distance(get_address(truck.truck_address), get_address(package.package_address))

            # check if the current package is closer than the previous closest neighbor - nearest neighbor algorithm
            if distance <= next_neighbor_distance:
                # update distance/package if the current package is closer
                next_neighbor_distance = distance
                next_neighbor_package = package




        # following code updates information for each singular package on each truck
        # assign next closest neighbor package to the truck package list
        truck.packages.append(next_neighbor_package.package_id)

        # remove next closest neighbor package from undelivered packages list
        undelivered_packages.remove(next_neighbor_package)

        # update truck total mileage with distance to next closest neighbor
        truck.miles += next_neighbor_distance
        # update truck current location to next neighbor package's address
        truck.truck_address = next_neighbor_package.package_address
        # get delivery time for the next neighbor package given speed = 18
        # this is the time of day value = time updated after every package is updated
        truck.time_of_day += datetime.timedelta(hours=next_neighbor_distance / 18)
        # set delivery times for the next neighbor package based on previous calculation
        next_neighbor_package.delivery_time = min(truck.time_of_day, truck.departure_time)
        # set delivery times for the next neighbor package based on previous calculation
        next_neighbor_package.delivery_time = truck.time_of_day
        # package leaves with truck
        next_neighbor_package.departure_time = truck.departure_time

        # assign truck number to the next neighbor package
        next_neighbor_package.truck_number = truck.truck_number


# update address for package 9 at 10:20
given_time_for_package_9 = datetime.timedelta(hours=10, minutes=20)
# look up package 9 info from hash table
package_9 = package_hash_table.lookup(9)
# update package 9's address based on the given time
package_9.update_package_9(given_time_for_package_9)

# calls deliver packages for truck 1
deliver_packages(Truck_1)

# calls deliver packages for truck 2
deliver_packages(Truck_2)

# calls deliver packages for truck 3
deliver_packages(Truck_3)

# print(Truck_1.departure_time)
# print(Truck_1.time_of_day)
# print(Truck_2.departure_time)
# print(Truck_2.time_of_day)
# print(Truck_3.departure_time)
# print(Truck_3.time_of_day)

# create Main class - User Interface
class Main:

    # prints on run
    print("Thank you for choosing WGUPS Routing Services")
    print()
    print("The total miles traveled is: ")
    # calculates and prints total miles
    print(Truck_1.miles + Truck_2.miles + Truck_3.miles)
    print()

    # asks user to START program
    text = input("Type START to begin search: ")
    # checks input is START
    if text.upper() == "START":
        # loop to keep asking for input
        while True:
            try:
                # asks user to input time to check
                user_time = input("Enter a time to check package status (HH:MM): ")
                # splits input to format
                (h, m) = user_time.split(":")
                # convert input
                given_time = datetime.timedelta(hours=int(h), minutes=int(m))
                # asks user to PACKAGE or ALL
                second_text = input("Type PACKAGE to see information for an individual package. Type ALL to see information for all packages. Type QUIT to exit: ")
                # checks input is PACKAGE
                if second_text.upper() == "PACKAGE":
                    try:
                        # takes int of ID input
                        package_input = int(input("Enter a package ID between 1 and 40: "))
                        # iterate through package IDs
                        for packageID in range(1, 41):
                            # look up in hash table by ID
                            package = package_hash_table.lookup(packageID)
                            # update delivery status given inputted time
                            package.update_status(given_time)

                            # check if the package is package 9 and the user input time is before 10:20
                            if package.package_id == 9 and given_time < datetime.timedelta(hours=10, minutes=20):
                                # set the old address for Package 9
                                package.package_address = "300 State St"
                                package.city = "Salt Lake City"
                                package.state = "UT"
                                package.zip_code = "84103"
                            # check if the package is package 9 and the user input time is after 10:20
                            if package.package_id == 9 and given_time >= datetime.timedelta(hours=10, minutes=20):
                                # set the new address for Package 9
                                package.package_address = "410 S State St"
                                package.city = "Salt Lake City"
                                package.state = "UT"
                                package.zip_code = "84111"

                            # check if package ID = user input
                            if package.package_id == package_input:
                                # print the package info
                                print(package)
                    except ValueError:
                        # prints if input wrong
                        print("Entry invalid. Please try again.")
                # check input is ALL
                elif second_text.upper() == "ALL":
                    try:
                        # iterate through package IDs
                        for packageID in range(1, 41):
                            # look up in hash table by ID
                            package = package_hash_table.lookup(packageID)
                            # update delivery status given inputted time
                            package.update_status(given_time)

                            # check if the package is package 9 and the user input time is before 10:20
                            if package.package_id == 9 and given_time < datetime.timedelta(hours=10, minutes=20):
                                # set the old address for Package 9
                                package.package_address = "300 State St"
                                package.city = "Salt Lake City"
                                package.state = "UT"
                                package.zip_code = "84103"
                            # check if the package is package 9 and the user input time is after 10:20
                            if package.package_id == 9 and given_time >= datetime.timedelta(hours=10, minutes=20):
                                # Set the new address for Package 9
                                package.package_address = "410 S State St"
                                package.city = "Salt Lake City"
                                package.state = "UT"
                                package.zip_code = "84111"

                            # print all package info
                            print(package)
                    except ValueError:
                        # print if input wrong
                        print("Entry invalid. Please try again.")
                # checks if input QUIT
                elif second_text.upper() == "QUIT":
                    print("Exiting program.")
                    # breaks out of loop
                    break
                else:
                    # print if input wrong
                    print("Entry invalid. Please try again.")
            except ValueError:
                # print if input wrong
                print("Entry invalid. Please try again.")
    else:
        # print if input wrong
        print("Entry invalid. Closing program.")