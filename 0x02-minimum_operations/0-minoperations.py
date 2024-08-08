#!/usr/bin/python3
"""a method that calculates the fewest number of operations needed"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
            Returns an integer
            If n is impossible to achieve, return 0
    """

    # If n is less than 2, return 0 because its impossible
    # to achieve n H characters
    if (n < 2):
        return 0

    oper = 0
    divisor = 2

    # Continue while n is greater than 1
    while (n > 1):
        if (n % divisor == 0):
            # If so, repeatedly divide n by the divisor
            # and add the divisor to operations
            while (n % divisor == 0):
                oper = oper + divisor
                n = n / divisor
            # move to the next potential divisor
            divisor = divisor + 1

    return oper
