Sure, here's a simple GitHub README for the "Making Change" problem:

---

# Making Change

## Problem Description
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Function Signature
```python
def makeChange(coins, total) -> int:
    pass
```

### Input
- `coins`: A list of the values of the coins in your possession.
- `total`: The amount total to be made with the coins.

### Output
- The fewest number of coins needed to meet the total.
- If the total is 0 or less, return 0.
- If the total cannot be met by any number of coins you have, return -1.

## Example
```python
makeChange([1, 2, 25], 37)   # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)   # Output: -1
```

## Approach
- This problem can be solved using dynamic programming.
- We initialize a dynamic programming array (`dp`) to store the minimum number of coins needed to make each value from 0 to the target total.
- We iterate through each coin denomination and update the `dp` array for each value from the coin value to the total.
- Finally, we return `dp[total]` if it's not infinity (indicating the total can be met), otherwise, we return -1.

---
