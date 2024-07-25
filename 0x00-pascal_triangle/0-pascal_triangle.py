#!/usr/bin/python3
"""Pascal's Triangle module"""


def pascal_triangle(n):
    """
    A function that returns a list of integers
      Args:
        n (int): The number of rows of the triangle
      Returns:
        List of lists of integers representing the Pascal's triangle
      """
    tri_list = []

    if n == 0:
        return tri_list

    # Generating pascal's triangle rows
    for i in range(n):
        if i == 0:
            tri_list.append([1])
        else:
            tri_list.append([])
            tri_list[i].append(1)
            for j in range(1, i):
                tri_list[i].append(tri_list[i - 1][j - 1] + tri_list[i - 1][j])
            tri_list[i].append(1)

    return tri_list
