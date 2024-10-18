#!/usr/bin/python3
"""
Prime Game
"""


def thePrimes(n):
    """
    list of prime less than n
    """
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] is True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i] and i >= 2]


def isWinner(x, nums):
    """
    determine the winner at the end of rounds
    """
    maria = 0
    ben = 0

    for n in nums:
        print(len(thePrimes(n)))
        if len(thePrimes(n)) % 2 == 0:
            ben = ben + 1
        else:
            maria = maria + 1
        # print(maria, ben)
    if ben > maria:
        return 'Ben'
    return 'Maria'

# print(isWinner(5, [2, 5, 1, 4, 3]))
