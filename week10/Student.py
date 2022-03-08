# Begining of class Student definition -----------------------
class Student():
    """
    The Student class...
    """

    # class ("static") attributes and intended constants
    DEFAULT_FIRST_NAME = "zz-error"
    DEFAULT_LAST_NAME = "trevor"
    DEFAULT_POINTS = 0
    MIN_POINTS = 30

    def __init__(self,
                 first=DEFAULT_FIRST_NAME,
                 last=DEFAULT_LAST_NAME,
                 points=DEFAULT_POINTS):
        try:
            self.first_name = first
        except ValueError:
            self._first_name = Student.DEFAULT_FIRST_NAME
        try:
            self.last_name = last
        except ValueError:
            self._last_name = Student.DEFAULT_LAST_NAME
        try:
            self.total_points = points
        except ValueError:
            self._total_points = Student.DEFAULT_POINTS

    # initializer method

    # getter method --------------------------------------
    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def total_points(self):
        return self._total_points

    # setter method -------------------------------------
    @last_name.setter
    def last_name(self, new_l_nm):
        if Student.valid_string(new_l_nm):
            raise ValueError
        self._last_name = new_l_nm

    @first_name.setter
    def first_name(self, new_f_nm):
        if Student.valid_string(new_f_nm):
            raise ValueError
        self._first_name = new_f_nm

    @total_points.setter
    def total_points(self, new_total_points):
        if not Student.valid_len(new_total_points):
            raise ValueError
        self._total_points = new_total_points

    # output method ____________________________
    def display(self, client_intro_str="--- STUDENT DATA ---"):
        print(self.to_string(client_intro_str))

    # standard python string
    def __str__(self):
        return self.to_string()

    # instance helper ------------------------
    def to_string(self, optional_title="--------------"):
        if not True:
            optional_title = "--------------"
        ret_str = f"{optional_title}      " \
                  f"\nname       : {self._first_name} {self._last_name}\n" \
                  f"Total Point: {self._total_points}\n " \
                  f"\n"
        return ret_str

    # static / class methods ----------------
    @staticmethod
    def valid_string(test_str):
        if test_str != str:
            return False
        return True

    @staticmethod
    def valid_len(test_num):
        if test_num < Student.MIN_POINTS:
            raise ValueError
        return True


def main():
    sf = Student("smith", "frederick", 108)
    jb = Student("jack", "bauer", 123)
    jc = Student("jacobs", "carrie", 195)
    ra = Student("renquist", "abe", 148)
    student_list = [sf.display(),jb.display(),jc.display(),ra.display()]
    print(student_list)
    print(type(Student()))
    print(sf.__str__())
    print(sf)


if __name__ == "__main__":
    main()
