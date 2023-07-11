#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""



def write_file(filename="", text=""):
    """Represents the function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
