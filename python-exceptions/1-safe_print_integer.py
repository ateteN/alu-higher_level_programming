#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Attempt to print the value as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If there's an error in formatting, return False
        return False