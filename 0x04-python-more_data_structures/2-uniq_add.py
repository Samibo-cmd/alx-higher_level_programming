#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = set(my_list)
    add_result = 0

    for i in unique_integers:
        add_result += i
    return (add_result)
