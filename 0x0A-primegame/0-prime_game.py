#!/usr/bin/python3
""" a module to determine who the winner of each of the prime game"""


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    if not nums or x < 1:
        return None
    max_no = max(nums)

    is_prime = [True for _ in range(max(max_no + 1, 2))]
    for n in range(2, int(pow(max_no, 0.5)) + 1):
        if not is_prime[n]:
            continue
        for m in range(n * n, max_no + 1, n):
            is_prime[m] = False
    is_prime[0] = is_prime[1] = False
    i = 0
    for n in range(len(is_prime)):
        if is_prime[n]:
            i += 1
        is_prime[n] = i
    player1_score = 0
    for x in nums:
        player1_score += is_prime[x] % 2 == 1
    if player1_score * 2 == len(nums):
        return None
    if player1_score * 2 > len(nums):
        return "Maria"
    return "Ben"
