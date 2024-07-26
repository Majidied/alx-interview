#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet a
    given amount of change.

    Parameters:
    coins (List[int]): A list of integers representing the available
    coin denominations.
    total (int): The total amount of change needed.

    Returns:
    int: The minimum number of coins needed to make the change,
    or -1 if it's not possible.
    """
    if total <= 0:
        return 0
    if coins is None or len(coins) == 0:
        return -1

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
