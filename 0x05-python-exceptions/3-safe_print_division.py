#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        operation = a / b
    except (TypeError, ZeroDivisionError):
        operation = None
    finally:
        print("Inside result:{}".format(operation))
    return (operation)
