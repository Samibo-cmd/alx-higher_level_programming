#!/usr/bin/python3
"""Defines a class named MyInt that inherits from int."""


class MyInt(int):
    """Inverts int operators."""

    def __eq__(self, value):
        """Overrides == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operator with == behavior."""
        return self.real == value
