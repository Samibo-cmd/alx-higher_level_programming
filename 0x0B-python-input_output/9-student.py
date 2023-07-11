#!/usr/bin/python3
"""Defines a class called Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student."""
        return self.__dict__