# This was level 5/Lyft problem.

# INT
# get(key)
# set(key, val)

# c = cache(2)
# c.set(1, 1) // None
# c.set(2, 2)
# c.get(2) // 2
# c.set(3, 3) // evict 1
# c.get(2) // -1


# This class implements a Hash-Map that keeps track of its size. Every entry will also have a usage metric so that
# when a user tries to put something into the map above the current size it will eject the least used entry to make
# room.


# Possible optimization to evicting. Have a hashmap whose key is the usage and points to the rest of the elements.
# Then when you evict you simply choose first one in the lowest tier.

# N -> They told me this is some mini-piece of a thing they wrote for caching jobs in a CI environment. Cool.
class usage_map:

    # Keep a global least used entry so when you set over the cache limit you can immediately eject
    # the first entry with that total.
    least_used =

    # Constructor, user passes the size they want for the object to contain.
    def __init__(self,size):
        self.internal_dict = {}
        self.size = size

    # When you set a value, check the size and make sure you don't need to evict.
    # If you do, use evict logic, if not add it and increment size.
    def set(self,key,value):

        # print("I'm currently trying to set the following key and value: " + str(key) + " " + str(value))

        # If your length is equal to your internal size you need to evict the least used entry.
        if len(self.internal_dict) == self.size:
            least_used = 999999
            least_used_index = None
            for element in self.internal_dict:
                # If you find an entry used less then current record, update.
                if self.internal_dict[element][1] < least_used:
                    least_used = self.internal_dict[element][1]
                    least_used_index = element
            # Get rid of the least used entry, then add the new entry.
            # Apparently dictionaries have an internal keyword to delete entries.
            del self.internal_dict[least_used_index]
            self.internal_dict[key] = (value,0)
        else:
            # Insert key and value and set usage as third index which starts at zero.
            self.internal_dict[key] = (value,0)

    # When you get a value, retrieve the value and increment internal usage count.
    def get(self, key):
        # Fetch current value of usage tuple then re-assign
        current_value = self.internal_dict[key][0]
        new_usage = self.internal_dict[key][1]
        new_usage += 1
        # print("The current usage of this entry is: " + str(self.internal_dict[key][1]))
        # Set new tuple to be current value and updated usage, then return.
        self.internal_dict[key] =  (current_value, new_usage)
        return current_value

    # Helper function for debugging that returns the internal dictionary.
    def get_dict(self):
        return self.internal_dict



some_new_map = usage_map(2)

# print("The size var of my new class is: " + str(some_new_map.size))

some_new_map.set(1,1)
some_new_map.set(2,2)
print("After two additions object is: " + str(some_new_map.get_dict()))
print("Getting new value at key 2 in class gives me: " + str(some_new_map.get(2)))
some_new_map.set(3,3)
print("After first possible eviction object is: " + str(some_new_map.get_dict()))



