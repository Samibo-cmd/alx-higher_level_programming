#!/usr/bin/python3

def number_keys(a_dictionary):
    key_count = 0
    dictionary_key = list(a_dictionary.keys())

    for i in dictionary_key:
        key_count += 1
    return (key_count)
