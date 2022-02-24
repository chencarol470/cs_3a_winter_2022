"""
File: arrays.py

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, item_type, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.item_type = item_type
        self.capacity = capacity
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return 'contents = ' + str(self.items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self.items)

    def getitem(self, index):
        """Subscript operator for access at index."""
        if index < self.capacity and index > 0:
            return self.items[index]
        else:
            return("index out of range")

    def setitem(self, index, newItem):
        """Subscript operator for replacement at index."""
        if type(newItem) == self.item_type:
            if index < self.capacity and index > 0:
                self.items[index] = newItem
            else:
                print("index out of range")
        else:
            print("Invalid Item type")