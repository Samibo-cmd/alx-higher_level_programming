#!/usr/bin/python3
"""Defines an inherited list named class MyList."""


class MyList(list):
    """Implements sorted printing"""

    def print_sorted(self):
        """ that prints the list, but sorted (ascending sort)."""
        print(sorted(self))
