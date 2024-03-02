#!/usr/bin/python3
""" The coin change problem """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount
    """
    # # Sort the coins in reverse order
    # coins.sort(reverse=True)

    # if total <= 0:
    #     return 0

    # # array to store minimum number of coins needed
    # dp = [float('inf')] * (total + 1)
    # # base case
    # dp[0] = 0

    # # Iterate through the various denominations
    # for coin in coins:
    #     for i in range(coin, total + 1):
    #         # Update minimum number of coins for each value
    #         dp[i] = min(dp[i], dp[i - coin] + 1)

    # return dp[total] if dp[total] != float('inf') else -1

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    i = 0
    count = 0

    while i < len(coins):
        count += total // coins[i]
        total = total % coins[i]
        i += 1
        if total == 0:
            return count

    return -1
