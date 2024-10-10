#!/usr/bin/python3
"""
Compute the perimeter of island
"""


def island_perimeter(grid):
    """
    Compute the perimeter of island
    """
    perim = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                perim = perim + 4
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perim = perim - 1
                if i > 0 and grid[i - 1][j] == 1:
                    perim = perim - 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perim = perim - 1
                if j > 0 and grid[i][j - 1] == 1:
                    perim = perim - 1
    return perim
