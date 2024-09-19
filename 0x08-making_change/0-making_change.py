#!/usr/bin/python3
"""
module to  determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    take a list of coins and use it
    to calculate how many needed to meet a given amount total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        coin_count = 0
        for n in coin:
            while(total >= n):
                coin_count += 1
                total -= n
        if total == 0:
            return coin_count
        return -1
