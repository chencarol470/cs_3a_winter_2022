# various_nums = [77.5, 92, 80, -78.111, 690, 101.3, -3.1515027, 0.0003, 23443]
#
# for index in range (len(various_nums)):
#     print(f"Item# {index} is {various_nums[index]}")
#     print(f"item# {index} is {various_nums[index]:+}")
#     print(f"item# {index} is {various_nums[index]: }")
#     print(f"item# {index} is {various_nums[index]:<20.7f}")
#     print(f"item# {index} is {various_nums[index]:>20.7f}")
#     print(f"item# {index} is {various_nums[index]:20.7f}")
#     print(f"item# {index} is {various_nums[index]:^20,.7f}")
#     print("=" * 30)
#
#
# def draw_dot(length, width, color):
#     pen = color()
#     pen.move = length
#     pen.left = width
#
#
# name1 = "jay"
# name2 = "alexandre"
# name3 = 1234
# print(f"Hello {name1:5}")
# print(f"Hello {name2:5}")
# print(f"Hello {name3:5}")

class Student():
    DEFAULT_NAME = "zzz"

    def __init__(self, nm=DEFAULT_NAME):
        try:
            self.name = nm
        except ValueError:
            self._name = Student.DEFAULT_NAME
    #
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, new_name):
    #     if 0 > len(new_name) or len(new_name) > 5:
    #         raise ValueError
    #     self._name = new_name


new_stu = Student("zad")
new_stu3 = Student("Kanle in the rain")
print(hex(id(Student.DEFAULT_NAME)), Student.DEFAULT_NAME)
print(hex(id(new_stu.name)), new_stu.name)
print(hex(id(new_stu.DEFAULT_NAME)), new_stu.DEFAULT_NAME)
# print(hex(id(Student.name)), Student.name)
print("=" * 30)
print(hex(id(Student.DEFAULT_NAME)), Student.DEFAULT_NAME)
print(hex(id(new_stu3.name)), new_stu3.name)
print(hex(id(new_stu3.DEFAULT_NAME)), new_stu3.DEFAULT_NAME)
# print(hex(id(Student.name)), Student.name)


