#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    function that returns the perimeter
    of the island described in grid
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for j, row in enumerate(grid):
        m = len(row)
        for k, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                j == 0 or (len(grid[j - 1]) > k and grid[j - 1][k] == 0),
                k == m - 1 or (m > k + 1 and row[k + 1] == 0),
                j == n - 1 or (len(grid[j + 1]) > k and grid[j + 1][k] == 0),
                k == 0 or row[k - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
