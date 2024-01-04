#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal's triangle of n

    Args:
        n (int): Integer representing triangle height
    """
    # Check if n is valid
    if n <= 0:
        return []

    # Create an empty triangle
    triangle = []

    # Generate each row and append to triangle
    for row_number in range(1, n + 1):
        # initialize each row with 1
        row = [1]

        # Generate values for the row
        for i in range(1, row_number - 1):
            value = triangle[row_number - 2][i - 1] + \
                triangle[row_number - 2][i]
            row.append(value)

        if row_number > 1:
            row.append(1)
        triangle.append(row)

    return triangle
