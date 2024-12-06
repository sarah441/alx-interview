#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Args:0(water) or 1(land)
    Returns:
         perims
    """

    p = 0
    for o in range(len(grid)):
        for j in range(len(grid[o])):
            if (grid[o][j] == 1):
                if (o <= 0 or grid[o - 1][j] == 0):
                    p += 1
                if (o >= len(grid) - 1 or grid[o + 1][j] == 0):
                    p += 1
                if (j <= 0 or grid[o][j - 1] == 0):
                    p += 1
                if (j >= len(grid[i]) - 1 or grid[o][j + 1] == 0):
                    p += 1
    return p
