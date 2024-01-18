#!/usr/bin/python3

def minOperations(n):
    """
    Returns the fewest number of operations needed to get to n
    """
    if n <= 0:
        return 0

    operations = 0
    clipboard = 1
    current_length = 1

    while current_length < n:
        # If current_length is a divisor of n, perform a copy operation
        if n % current_length == 0:
            clipboard = current_length
            operations += 1

        # Perform a paste operation
        current_length += clipboard
        operations += 1

    return operations if current_length == n else 0
