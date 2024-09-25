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

    # validate input is a list of lists
    if type(grid) != list:
        return 0
    n = len(grid)  # the number of rows in the grid
    for r, row in enumerate(grid):
        m = len(row)  # the number of columns in the current row
        for c, cell in enumerate(row):
            if cell == 0:
                continue
            # see edges to determine how many sides contribute with perimeter
            edges = (
                r == 0 or (len(grid[r - 1]) > c and grid[r - 1][c] == 0),
                c == m - 1 or (m > c + 1 and row[c + 1] == 0),
                r == n - 1 or (len(grid[r + 1]) > c and grid[r + 1][c] == 0),
                c == 0 or row[c - 1] == 0,
            )
            # add the number of edges that are part of the perimeter
            perimeter += sum(edges)
    return perimeter
