def factorial(n):
    print(n)
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def fact_iter(n):
    for i in range(n):
        pass





def fact(n):
    """
    Returns factorial of n (n!).
    Note use of recursion
    """

    # BASE CASE!
    if n == 0:
        return 1

    # Recursion!
    else: return n * fact(n-1)