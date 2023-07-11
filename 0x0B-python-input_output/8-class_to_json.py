#!/usr/bin/python3
"""Defines a Python called class-to-JSON function."""


def class_to_json(obj):
    """Returns dictionary represntation of a simple data structure."""
    return obj.__dict__
