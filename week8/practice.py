# class Employee:
#     nm = "undefined"
#     age = 0
#
#     # Initializer method -------
#     def __init__(self, the_name=nm, the_age=age):
#         self._the_name = the_name
#         self._the_age = the_age
#
#     # getter method-----------------
#     @property
#     def the_nm(self):
#         return self._the_name
#
#     @property
#     def the_age(self):
#         return self._the_age
#
#     # setter method----------------
#     @the_nm.setter
#     def the_nm(self, new_name):
#         if len(new_name) > 10:
#             return False
#         self._the_name = new_name
#         return True
#
#     @the_age.setter
#     def the_age(self,new_age):
#         if new_age < 0:
#             return False
#         self._the_age = new_age
#         return True
#
#
# user_name = input("Enter your name. ")
# user_age = input("Enter your age. ")
# new_user = Employee(user_name,user_age)
# print(new_user.the_nm,new_user.the_age)
#

messege = "        learn python         "
print("Message", messege.strip())
print("Message", messege)