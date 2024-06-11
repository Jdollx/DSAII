# create Hash class
class CreateHashTable:

    # constructor to initialize an empty hash table for 0-39 index (40 packages)
    # SOURCE: C950 - Webinar-1 - Let's Go Hashing
    def __init__(self, initial_capacity = 39):
        # initialize hash table with empty lists
        self.table = []
        # iterate through given range
        for i in range(initial_capacity):
            # add empty list to each index in the hash table
            self.table.append([])

    # method to insert package into table
    def insert(self, key, item):
        # assigns package to buckets using hash function
        bucket = hash(key) % len(self.table)
        # get list of items in the given bucket
        bucket_list = self.table[bucket]

        # check if key (ID) already in bucket
        # SOURCE: C950 - Webinar-2 - Getting Greedy, who moved my data?
        for kv in bucket_list:
            if kv[0] == key:
                # update item with new package info
                kv[1] = item
                return True

        # adds package to end of bucket_list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # method to search table with key to return item
    def search(self, key):
        # assigns package to buckets using hash function
        bucket = hash(key) % len(self.table)
        # get list of items in the given bucket
        bucket_list = self.table[bucket]

        # iterate through kv pairs in bucket list
        # SOURCE: C950 - Webinar-2 - Getting Greedy, who moved my data?
        for kv in bucket_list:
            # check if iteration key matches input key
            if kv[0] == key:
                # return value
                return kv[1]
        return None

    # removes a package if package ID is already in the table
    def remove(self, key):
        # assigns package to buckets using hash function
        bucket = hash(key) % len(self.table)
        # get list of items in the given bucket
        bucket_list = self.table[bucket]

        # iterate through kv pairs in bucket list
        for kv in bucket_list:
            # check if iteration key matches input key
            if kv[0] == key:
                # remove kv pair for given key
                bucket_list.remove(kv[0], kv[1])

    # look up items in hash table by key
    # SOURCE: Python: Creating a HASHMAP using Lists (https://www.youtube.com/watch?v=9HFbhPscPU0&ab_channel=OggiAI-ArtificialIntelligenceToday)
    # SOURCE: C950 - Webinar-1 - Let's Go Hashing
    def lookup(self, key):
        # assigns package to buckets using hash function
        bucket = hash(key) % len(self.table)
        # get list of items in the given bucket
        bucket_list = self.table[bucket]

        # iterate through kv pairs in bucket list
        for kv in bucket_list:
            # check if iteration key matches input key
            if key == kv[0]:
                # return value
                return kv[1]
        return None









