#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """ Check if a number is prime """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def calculate_primes(n, primes):
    """ Calculate primes """
    if n <= 1:
        return 0
    if primes[n] == 1:
        return 1
    if primes[n] == 0:
        return 0
    if is_prime(n):
        primes[n] = 1
        return 1
    primes[n] = 0
    return 0


def isWinner(x, nums):
    """ Prime Game """
    primes = [2 for _ in range(max(nums) + 1)]
    calculate_primes(max(nums), primes)
    maria = 0
    ben = 0
    for n in nums:
        count = 0
        for i in range(2, n + 1):
            count += calculate_primes(i, primes)
        if count % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria < ben:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
