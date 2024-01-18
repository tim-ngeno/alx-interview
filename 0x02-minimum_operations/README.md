# MinOperations

## Problem Statement

Given a text file containing a single character 'H', design a method to calculate the fewest number of operations required to achieve exactly 'n' occurrences of 'H' in the file. The only allowed operations are Copy All and Paste. If it is impossible to achieve 'n' occurrences, return 0.

## Solution

The solution is implemented in Python and consists of a function `minOperations(n)`. This function takes an integer 'n' as input and calculates the minimum number of operations needed to obtain 'n' occurrences of 'H' in the file.

### Approach

The algorithm employs a dynamic programming approach, iterating through possible lengths of the file and updating the minimum operations accordingly. The allowed operations include Copy All and Paste. The function returns the minimum number of operations needed, or 0 if it is impossible to achieve 'n' occurrences.

### Example

```python
n = 9
result = minOperations(n)
print("Min # of operations to reach {} char: {}".format(n, result))
```

Output:
```
Min # of operations to reach 9 char: 6
```

---
