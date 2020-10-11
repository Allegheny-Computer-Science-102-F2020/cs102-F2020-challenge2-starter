"""Print values and lists of values."""

from typing import List


def convert_bool_to_answer(argument: bool):
    """Return a string-based and human-readable representation of a bool."""
    if argument:
        return "Yes"
    return "No"


def display_list(values: List, indent=""):
    """Display the provided list when iterating and printing every indented value."""
    # TODO: make sure that you understand how this
    # iteration construct operators on tuples
    # iterate through all of the tuples that contain the
    # ordered pairs of the form (i, 2**i)
    for index, value in values:
        print(f"{indent}2**{index} = {value}")
