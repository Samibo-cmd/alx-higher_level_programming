#!/usr/bin/python3
"""Defines a class named Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes a new Rectangle with two attributes."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
