
# Prime Game

## Problem Description

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

### Function Signature

```python
def isWinner(x, nums):
    pass
```

### Inputs

- `x`: An integer representing the number of rounds to be played.
- `nums`: A list of integers representing the value of n for each round.

### Outputs

- The name of the player who won the most rounds.
- If the winner cannot be determined, return `None`.

## Example

```python
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
# Output: "Maria"
```

## Implementation Details

1. The function `primes_up_to(n)` generates all prime numbers up to n using the Sieve of Eratosthenes algorithm.
2. The function `get_winner(round_num, primes)` determines the winner of each round by considering the available prime numbers and ensuring both players make optimal moves.
3. The main function `isWinner(x, nums)` iterates over each round, calculates the winner for each round, and keeps track of the number of wins for each player.
4. Finally, it determines the overall winner based on the number of wins.

## Usage

- Call the function `isWinner(x, nums)` with the desired number of rounds `x` and the list of values `nums` representing `n` for each round.
- The function returns the name of the player who won the most rounds, or `None` if the winner cannot be determined.

---
