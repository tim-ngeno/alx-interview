#!/usr/bin/python3
""" NQueens Puzzle """

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, solutions):
    """
    Recursive utility function to solve N queens problem
    """
    if row == len(board):
        solutions.append([x[:] for x in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, solutions)
            board[row][col] = 0


def solve_nqueens(n):
    """
    Solve the N queens problem
    """
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def print_solutions(solutions):
    """
    Print all solutions to the problem
    """
    for solution in solutions:
        transformed_solution = []
        for row_idx, row in enumerate(solution):
            for col_idx, val in enumerate(row):
                if val == 1:
                    transformed_solution.append([row_idx, col_idx])
        print(transformed_solution)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater than or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    solutions = solve_nqueens(N)

    # Print the solutions
    print_solutions(solutions)
