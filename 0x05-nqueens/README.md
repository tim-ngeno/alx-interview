
# N Queens

The N queens problem is a classic problem in the field of computer science and combinatorial optimization. The challenge is to place N non-attacking queens on an N×N chessboard, where no two queens share the same row, column, or diagonal.

This repository provides a Python script to solve the N queens problem and print every possible solution to the problem. The solution utilizes backtracking to systematically explore all possible placements of queens on the chessboard.

## Usage

To use the N queens problem solver, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone <repository_url>
```

2. Navigate to the directory containing the Python script:

```bash
cd <repository_directory>
```

3. Run the script with the desired value of N as an argument. For example, to solve the N queens problem for N = 4:

```bash
python nqueens.py 4
```

Replace `4` with the desired value of N. Note that N must be an integer greater than or equal to 4.

## Example

```bash
python nqueens.py 4
```

Output:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Each line represents a solution to the N queens problem, where each pair of numbers represents the row and column coordinates of a queen on the chessboard.

## Constraints

- The script accepts only one command-line argument, which is the value of N.
- N must be an integer greater than or equal to 4.
- If the user provides the wrong number of arguments or an invalid value for N, appropriate error messages will be displayed.

## Implementation Details

The solution is implemented in Python and utilizes backtracking to explore all possible placements of queens on the chessboard. The program checks if it's safe to place a queen in a particular position by verifying that no other queen threatens it along the row, column, or diagonal. Solutions are printed in a specific format, with each line representing a placement of queens on the chessboard.
---
