class Dog:
    def __init__(self):
        self._wags_per_minute = 0
        self._name = "(unnamed dog)"

    def promise_piece_of_carrot(self):
        self.wags_per_minute *= 3

    @property
    def wags_per_minute(self):
        return self._wags_per_minute

    @wags_per_minute.setter
    def wags_per_minute(self, wags):
        self._wags_per_minute = wags

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def difference_in_wags(self, other_dog):
        return self.wags_per_minute - other_dog.wags_per_minute

# client --------------------------------------------
chloe = Dog()
chloe.name = "chloe"
chloe.wags_per_minute = 30

watson = Dog()
watson.name = "Watson the Waggiest"
watson.wags_per_minute = 75

print(f"The difference in wag frequency between {chloe.name} and {watson.name} is {chloe.difference_in_wags(watson)}")