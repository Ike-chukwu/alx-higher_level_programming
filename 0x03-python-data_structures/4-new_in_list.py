#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        output = my_list[:]
        output[idx] = element
        return output
    return my_list
