# beginning of class Frequency definition -------------------------
class Frequency:
    # class ("static") members and intended constants
    MAX_SIZE = 100000
    DEFAULT_SIZE = 26
    ERROR_RETURN_FREQ = -1

    # initializer method -------------------
    def __init__(self, size=DEFAULT_SIZE):

        # instance attributes
        if (not self.set_size(size)):
            self.size = Frequency.DEFAULT_SIZE

        # initialize an array of size frequencies, all to 0
        self.clear()

    # setters -------------------------------
    def set_size(self, size):
        if not self.valid_size(size):
            return False

        # else
        self.size = size
        # and re-initialize an array of new size frequencies, all to 0
        self.clear()
        return True

    # Inrease number of items
    def increment(self, index):
        if (not (0 <= index < self.size)):
            return False
        # else
        self.count[index] += 1
        return True

    def decrement(self, index):
        if not (
                (0 <= index < self.size)
                and (self.count[index] > 0)
        ):
            return False
        # else
        self.count[index] -= 1
        return True

    def clear(self):
        """ set all frequencies to 0 """
        self.count = [0 for k in range(self.size)]

    # getters -------------------------------
    def get_size(self):
        return self.size

    def get(self, index):
        if (not (0 <= index < self.size)):
            return self.ERROR_RETURN_FREQ
            # else
        return self.count[index]

    # static/class methods ------------------------
    @classmethod
    def valid_size(cls, test_size):
        if not (0 <= test_size <= cls.MAX_SIZE):
            return False
        else:
            return True


"""
This class provides methods for incrementing and decrementing the individual elements of the array, and also a getter to return any value in the array. 

It provides the following protections:
No direct client access encouraged due to a lack of setters for the frequency counts.
No attempts to increment or decrement an index outside the bounds of the array.
No accidental decrements below 0, since counts below 0 have no meaning.
Here is a nice use of this class: 
"""

# --- client -------------------------------------------
# instantiate a Frequency object
letters = Frequency(26)

# this block should leave a 27 in letter[2]
for k in range(28):
    letters.increment(2)
letters.decrement(2)

# this block should leave a 59 in letter[25]
for k in range(59):
    letters.increment(ord('Z') - ord('A'))  # this is 25, the 26th freq

# some illegal accesses
letters.decrement(500)
letters.increment(-3)

# display whole table, going "too far"
for k in range(-3, 30):
    # every 5 items, generate a newline
    if (k % 5 == 0):
        print()
    print(f"{k}:\t {letters.get(k)}\t   ", end='')

