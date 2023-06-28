#!/usr/bin/python3
"""Defines a class named square"""


class Square:
    """This is a class of square"""
    def __init__(self, size=0):
        """Initialise class with a size attributes"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
