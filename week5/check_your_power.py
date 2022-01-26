# home made power method ------------------------
def my_power(number, exp):
    if type(exp) != int:
        raise ValueError

    if (exp == 0):
        return 1
    if (exp < 0):
        return 1. / my_power(number, -exp)
    else:
        return number * my_power(number, exp - 1)


# client --------------------------------------
print(f"{my_power(2.4, 4)} v. {(2.4 ** 4)}")
print(f"{my_power(1.23, 9)} v. {(1.23 ** 9)}")
print(f"{my_power(5535, -29)} v. {(5535 ** -29)}")
print(f"{my_power(2., 32)} v. {(2. ** 32)}")
print(f"{my_power(4, 1.5)} v. {(4 ** 1.5)}")
