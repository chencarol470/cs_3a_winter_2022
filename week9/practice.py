# # program functions ---------------------------------
# def promise_piece_of_carrot(freq):
#     freq[0] *= 3
#     return freq
#
#
#
# # client --------------------------------------------
# chloes_wag_frequency = [30]
# print(f"Chloe's wag frequency is {chloes_wag_frequency} wags per minute.")
# promise_piece_of_carrot( chloes_wag_frequency)
# print(f"Chloe's wag frequency is {chloes_wag_frequency} wags per minute.")
#
#
# # program functions ---------------------------------
# def promise_piece_of_carrot(freq):
#     freq *= 3
#     return freq
#
#
# # client --------------------------------------------
#
# chloes_wag_frequency = 30
# print(f"Chloe's wag frequency is {chloes_wag_frequency} wags per minute.")
# promise_piece_of_carrot(chloes_wag_frequency)
# print(f"Chloe's wag frequency is {chloes_wag_frequency} wags per minute.")

class MyClass:
    def hello():
        # this IS intended to be an instance method, we just forgot to add a parameter to capture the instance
        # when this is called from an instance - so this will fail
        print('hello...')

    def instance_hello(arg):
        print(f'hello from {arg}')

    @classmethod
    def class_hello(arg):  # althose in this example we passed arg as parameter name in our method,
        # the normal convention to use is self or cls - that way, everyone knows what we're talking about.
        print(f'hello from {arg}')

m = MyClass()
try:
    m.hello()
except TypeError as ex:
    print(ex)

try:
    m.instance_hello()
except TypeError as ex:
    print(ex)
