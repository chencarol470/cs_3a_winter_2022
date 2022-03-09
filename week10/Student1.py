class Student:
    # class ("static") attributes and intended constants
    DEFAULT_NAME = "zz-error"
    DEFAULT_POINTS = 0
    MAX_POINTS = 30

    # initializer method -------------------
    def __init__(self,
                 last=DEFAULT_NAME,
                 first=DEFAULT_NAME,
                 points=DEFAULT_POINTS):
        # instance attributes

        try:
            self.last_name = last
        except ValueError:
            self._last_name = Student.DEFAULT_NAME

        try:
            self.first_name = first
        except ValueError:
            self._first_name = Student.DEFAULT_NAME

        try:
            self.total_points = points
        except ValueError:
            self._total_points = Student.DEFAULT_POINTS

    # accessor ("get") methods -------------------------

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def total_points(self):
        return self._total_points

    # mutator ("set") methods -----------------
    @last_name.setter
    def last_name(self, last):
        if not self.valid_string(last):
            raise ValueError
        self._last_name = last

    @first_name.setter
    def first_name(self, first):
        if not self.valid_string(first):
            raise ValueError
        self._first_name = first

    @total_points.setter
    def total_points(self, points):
        if not self.valid_point(points):
            raise ValueError
        self._total_points = points

    # output method ----------------------------------
    def display(self, client_into_str="--- STUDENT DATA ---"):
        print(client_into_str + str(self))

    # standard python stringizer ----------------------
    def __str__(self):
        return self.to_string()

    # instance helpers --------------------------------
    def to_string(self, optional_title="------------------------"):
        ret_str = (f"{optional_title}"
                   f"\n    name: {self.last_name}, {self.first_name}"
                   f"\n    total points: {self.total_points}.")
        return ret_str

    # def to_repr(self):
    #     ret_str = (f"representation "
    #                f"\n  class_id:{hex(self._first_name)}")
    #     return ret_str

    # static/class methods---------------------------------
    @staticmethod
    def valid_string(test_str):
        if (len(test_str) > 0) and test_str[0].isalpha():
            return True
        return False

    @classmethod
    def valid_point(cls, test_points):
        if 0 <= test_points <= cls.MAX_POINTS:
            return False
        return True

    @staticmethod
    def compare_strings_ignore_case(first_string, second_string):
        """ returns -1 if first < second, lexicographically,
                    +1 if first > second, and 0 if same
                    this particular version based on last name only
                    (case sensitive) """
        fst_upper = first_string.upper()
        scnd_upper = second_string.upper()
        if fst_upper < scnd_upper:
            return -1
        return 0


# beginning of class StudentArrayUtilities definition ---------------
class StudentArrayUtilities:
    @classmethod
    def print_array(cls, stud_array,
                    optional_title="--- The Students -----------:\n"):
        print(cls.to_string(stud_array, optional_title))

    @classmethod
    def array_sort(cls, data, array_size):
        for k in range(array_size):
            if not cls.float_largest_to_top(data, array_size - k):
                return

    # class stringizers ----------------------------------

    @staticmethod
    def to_string(stud_array,
                  optional_title="--- The Students -----------:\n"):
        ret_val = optional_title + "\n"
        for student in stud_array:
            ret_val = ret_val + str(student) + "\n"
        return ret_val

    @staticmethod
    def float_largest_to_top(data, array_size):
        changed = False

        # notice we stop at array_size - 2 because of expr. k + 1 in loop
        for k in range(array_size - 1):
            if Student.compare_strings_ignore_case(
                    data[k].last_name, data[k + 1].last_name) > 0:
                data[k], data[k + 1] = data[k + 1], data[k]
                changed = True

        return changed


def make_a_guest_student():
    return Student("Guest", "Student", 0)


def main():
    my_students = \
        [
            Student("smith", "frederick", 108),
            Student("jack", "bauer", 123),
            Student("jacobs", "carrie", 195),
            Student("renquist", "abe", 148),
        ]
    for index in range(len(my_students)):
        my_students[index].display()
        print(type(my_students[index]))
    # po = Student.to_repr()
    print(make_a_guest_student())


if __name__ == "__main__":
    main()
