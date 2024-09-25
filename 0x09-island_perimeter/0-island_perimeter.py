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
    for n in range(len(grid)):
        for m in range(len(grid[n])):
            if grid[n][m] == 1:
                perimeter += 4
                if m > 0 and grid[n-1][m] == 1:
                    perimeter -= 2
                if m > 0 and grid[n][m-1] == 1:
                    perimeter -= 2
    return perimeter
