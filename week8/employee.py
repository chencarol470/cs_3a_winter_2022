class Employee:
    """ learning getters and setters """

    # class ("static") attributes and intended constants
    DEFAULT_NAME = "(no name assigned)"
    DEFAULT_SS = "000000000"
    DEFAULT_AGE = 0

    MIN_AGE = 0
    MAX_NAME_LEN = 30

    emp_population = 0

    # initializer method -------------------------------
    def __init__(self,
                 the_nm=DEFAULT_NAME,
                 the_ss=DEFAULT_SS,
                 the_age=DEFAULT_AGE):
        # instance (attributes
        if not self.set_soc_sec(the_ss):
            self.soc_sec = Employee.DEFAULT_SS
        if not self.set_age(the_age):
            self.age = Employee.DEFAULT_AGE
        if not self.set_name(the_nm):
            self.name = Employee.DEFAULT_NAME

        Employee.emp_population += 1

    # setter ("set") methods -------------------------------
    def set_soc_sec(self, ss_num):
        if type(ss_num) != str or len(ss_num) != 9 or not ss_num.isdigit():
            return False
        # else
        self.soc_sec = ss_num
        return True

    def set_name(self, the_name):
        if type(the_name) != str or len(the_name) > Employee.MAX_NAME_LEN:
            return False
        # else
        self.name = the_name
        return True

    def set_age(self, the_age):
        if type(the_age) != int or the_age < Employee.MIN_AGE:
            return False
        # else
        self.age = the_age
        return True

    # getter methods -------------------------------
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_soc_sec(self):
        return self.soc_sec

    # other instance methods
    def clear_soc_sec(self):
        self.soc_sec = Employee.DEFAULT_SS

    def get_older(self):
        self.age += 1
        if self.age > 147:
            self.clear_soc_sec()
            return False
        else:
            return True


# client --------------------------------------------

# instantiate some employees with some illegal ss #s ...
emp_1 = Employee("too short", "999", 31)
emp_2 = Employee("has letter", "1234X6789", 32)
emp_3 = Employee("just right", "123466789", 33)
print(f"There are {Employee.emp_population} people working in the company.")

# show the employees
print(("Employee #1:"
       + "\n    name: {}"
       + "\n    age: {}"
       + "\n    ss#: {}").
      format(emp_1.get_name(), emp_1.get_age(),
             emp_1.get_soc_sec()))

print(("Employee #2:"
       + "\n    name: {}"
       + "\n    age: {}"
       + "\n    ss#: {}").
      format(emp_2.get_name(), emp_2.get_age(),
             emp_2.get_soc_sec()))

print(("Employee #3:"
       + "\n    name: {}"
       + "\n    age: {}"
       + "\n    ss#: {}").
      format(emp_3.get_name(), emp_3.get_age(),
             emp_3.get_soc_sec()))

""" --------------------------- RUN ---------------------------
Employee #1:
    name: too short
    age: 31
    ss#: 000000000
Employee #2:
    name: has letter
    age: 32
    ss#: 000000000
Employee #3:
    name: just right
    age: 33
    ss#: 123466789
------------------------------------------------------------ """


# class Employee():
#     # initializer method------------
#     def __init__(self,
#                  the_nm="(no name assigned)",
#                  the_ss="000000000",
#                  the_age=0):
#         self.name = the_nm
#         self.soc_sec = the_ss
#         self.age = the_age
#
#     # setter method -------------
#     def set_soc_sec(self, ss_num):
#         if type(ss_num) != str or len(ss_num) != 9 or not ss_num.isdigit():
#             return False
#         else:
#             self.soc_sec = ss_num
#             return True
#
#     def set_name(self, the_name):
#         if type(the_name) != str or len(the_name) > 30:
#             return False
#         else:
#             self.name = the_name
#             return True
#
#     def set_age(self, the_age):
#         if type(the_age) != int or the_age < 0:
#             return False
#         else:
#             self.age = the_age
#             return True
#
#     #getter------------
#     def get_name(self):
#         return self.name
#
#     def get_soc_sec(self):
#         return self.soc_sec
#
#     def get_age(self):
#         return self.age
#
#
# tim = Employee()
# tim.name, tim.age, tim.soc_sec = "Tim", -2, 12345678
# print(tim.name,tim.age,tim.soc_sec)
# print(tim.get_soc_sec(),tim.get_name(),tim.get_age())
#
# jim = Employee()
# jim.set_soc_sec("432")
# jim.set_name("JimSpongeIsCuteAndCoolBoyWeDon'tKnowThatIsReallyCoolMan.........................")
# jim.set_age(-6)
# #See below data en
# print(jim.get_name(),jim.get_age(),jim.get_soc_sec())
#
