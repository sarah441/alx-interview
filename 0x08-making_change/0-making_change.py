#!/usr/bin/python3

""" make ChangE"""


def makeChange(coins, total):
    """
    Returns: least coins needed
        If total is 0 return 0
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for i in coins:
        while i <= total:
            total -= i
            change += 1
        if (total == 0):
            return change
    return -1
