#!/usr/bin/python3
def remove_char_at(str, n):
    list1 = list(str)
    i = n
    for i in range(n, len[list1]):
        list1[i] = list1[i + 1]
    str = ''.join(list1)
    return str
