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
    divisor = 1
    count = 0

    # Continue while n is greater than divisor
    while (n > divisor):
        remain = n - divisor
        if (remain % divisor == 0):
            # If so, repeatedly divide remainder by the divisor
            # and add the divisor to operations
            oper = divisor
            divisor = divisor + oper
            count = count + 2
        else:
            divisor = divisor + oper
            count = count + 1

    return count
