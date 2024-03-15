#!/usr/bin/python3
""" Prime numbers game """


def primes_up_to(n):
    """Generate all prime numbers up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def isWinner(x, nums):
    """ Determines the winner of the prime game """
    def get_winner(round_num, primes):
        """ Helper function to get the winner """
        # If there are no prime numbers, Maria wins
        if not primes:
            return "Maria"

        # If the given number is prime, the player whose turn it is wins
        if nums[round_num] in primes:
            return "Maria" if round_num % 2 == 0 else "Ben"
        else:
            # Or the number of primes available
            count = sum(1 for p in primes if p <= nums[round_num])
            if count == 1:
                return "Maria" if round_num % 2 == 0 else "Ben"
            else:
                return "Ben" if count % 2 == 0 else "Maria"

    # Store the number of wins for each player
    maria_wins = ben_wins = 0

    # Generate primes up to the maximum possible n
    max_n = max(nums)
    all_primes = primes_up_to(max_n)

    # Iterate over each round
    for i in range(x):
        winner = get_winner(i, all_primes)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine the winner based on the number of wins
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
