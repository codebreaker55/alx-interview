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

    tot_opers = 0
    curr_chars = 1
    count = 0

    # Continue while n is greater than current characters
    while (n > curr_chars):
        remain = n - curr_chars
        if (remain % curr_chars == 0):
            # If so, repeatedly divide remainder by the current characters
            # and add the curr_chaars to the total operations
            tot_opers = curr_chars
            curr_chars = curr_chars + tot_opers
            count = count + 2
        else:
            # Otherwise, just add the current characters to the operations
            curr_chars = curr_chars + tot_opers
            count = count + 1

    return count
