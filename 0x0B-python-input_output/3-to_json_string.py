#!/usr/bin/python3
"""Defines a function that returns the JSON representation of object"""
import json


def to_json_string(my_obj):
    """Repurns the JSON representation of object"""
    return json.dumps(my_obj)
