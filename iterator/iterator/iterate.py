"""Calculate the powers of two, with iteration, from minimum to maximum values."""

# TODO: Add the required import statements for List and Tuple


def calculate_powers_of_two_for_loop(
    minimum: int, maximum: int
) -> List[Tuple[int, int]]:
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    powers_list = []
    # iterate through a sequence of numbers that range from
    # the minimum (inclusive) to the maximum (exclusive)
    for i in range(minimum, maximum):
        # TODO: save a two-tuple of the form (i, 2**i)
    # return the list of the tuples of the powers
    return powers_list


def calculate_powers_of_two_while_loop(
    minimum: int, maximum: int
) -> List[Tuple[int, int]]:
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    powers_list = []
    i = minimum
    # iterate through a sequence of numbers that range from
    # the minimum (inclusive) to the maximum (exclusive)
    while i < maximum:
        # TODO: save a two-tuple of the form (i, 2**i)
        i += 1
    # return the list of the tuples of the powers
    return powers_list
