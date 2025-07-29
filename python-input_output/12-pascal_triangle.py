#!/usr/bin/python3
"""
Function that returns a list of lists of integers representing Pascal’s triangle of n.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows of the triangle to generate.

    Returns:
        List[List[int]]: Pascal's Triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element

        # Compute inner elements
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Last element
        triangle.append(new_row)

    return triangle
