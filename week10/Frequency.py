# beginning of class Frequency definition----------
class Frequency:
    # class ("static") members and intended constants
    MAX_SIZE = 100000
    DEFAULT_SIZE = 26
    ERROR_RETURN_FREQ = -1

    # initializer method --------------------------
    def __init__(self, size=DEFAULT_SIZE):
        # instance attributes
        if not self.set_size(size):
            self.size = Frequency.DEFAULT_SIZE

        # initialize an array of size frequencies, all to 0
        self.clear()

    # setter -----------------------------------
    def set_size(self, new_size):
        if not self.valid_size(new_size):
            return False
        # else
        self.size = new_size
        # and re-initialize an array of new size frequencies, all to 0
        self.clear()
        return True

    def increment(self, index):
        if not (0 <= index <= self.size):
            return False
        # else
        self.count[index] += 1

    def decrement(self, index):
        if not ((0 <= index < self.size) and (self.count[index] > 0)):
            return False
        # else
        self.count[index] -= 1
        return True

    def clear(self):
        """ set all frequencies to 0 """
        self.count = [0 for k in range(self.size)]

    # getter -------------------------------------------
    def get_size(self):
        return self.size

    def get(self, index):
        if not (0 <= index < self.size):
            return self.ERROR_RETURN_FREQ
        # else
        return self.count[index]

    # static / class methods ------------------------
    @classmethod
    def valid_size(cls, test_size):
        if not 0 <= test_size <= cls.MAX_SIZE:
            return False
        else:
            return True


# beginning of class CharacterCounter definition -------------------------
class CharacterCounter:
    # class ("static") members and intended constants
    MAX_LEN = 100000
    MIN_LEN = 1
    DEFAULT_STR = " -- Default Test String -- "
    ERROR_RET_NUM = -1

    # initializer ("constructor") method -------------------
    def __init__(self, user_string=DEFAULT_STR):
        # instance attributes

        # default Frequency member object of size  26 to hold counts
        self.letters = Frequency()

        if (not self.set_my_string(user_string)):
            # use setter since it will do more than just mutate (unusual)
            self.set_my_string(DEFAULT_STR)

    # setters -------------------------------
    def set_my_string(self, user_string):

        if not self.valid_string(user_string):
            return False
        self.my_string = user_string

        # as soon as it's born or changes, count new string anew
        self.count_occurences()
        return True

    # getters -----------------------------
    def get_my_string(self):
        return self.my_string

    def get_count(self, letter):
        # note that error return is passed up in expression below illegal
        return self.letters.get(ord(letter.upper()) - ord('A'))

    # helpers --------------------------------
    def count_occurences(self):
        # reset letters[] to all 0 in case used before by last my_string
        self.letters.clear()

        # upcase for case insenstive counts (or don't for case sensitive)
        work_string = self.my_string.upper()
        str_len = len(work_string)

        for let in work_string:
            self.letters.increment(ord(let) - ord('A'))

    @classmethod
    def valid_string(cls, test_string):
        if not (0 <= len(test_string) <= cls.MAX_LEN):
            return False
        else:
            return True


# client --------------------------------------------

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
    print("{: }: {: }   \t".format(k, letters.get(k)), end='')

user_phrase = input("\nEnter a phrase or sentence: ")

# create a CharacterCounter object for this phrase
freq = CharacterCounter(user_phrase)

# display whole table
for k in range(ord('A'), ord('Z') + 1):

    # convert k to kth letter in ABCD ... Z
    let = chr(k)

    # every 5 items, generate a newline
    if (k % 5 == 0):
        print()
    print("{}: {: }   \t".format(let, freq.get_count(let)), end='')
