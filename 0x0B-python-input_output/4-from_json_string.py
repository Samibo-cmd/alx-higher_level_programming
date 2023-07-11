#!/usr/bin/python3
"""Defines a function that returns an object represented by a json string"""
import json


def from_json_string(my_str):
    """Returns a json string"""
    return json.loads(my_str)
