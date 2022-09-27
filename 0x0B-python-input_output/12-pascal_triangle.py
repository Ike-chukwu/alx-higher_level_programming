#!/usr/bin/python3
"""
Pascal triangle def.
"""

def pascal_triangle(n):
    """function to make it"""
    if n <= 0:
        return []

    p_t = [[1]]
    for i in range(2, n+1):
        tmp = [0] + p_t[i-2] + [0]
        p_t.append([sum(par) for par in zip(tmp, tmp[1:])])
    return p_t
