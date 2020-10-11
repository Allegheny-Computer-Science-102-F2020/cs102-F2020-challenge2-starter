"""Test the functions that calculate powers of 2 to ensure they work correctly."""

from iterator import iterate


def test_for_loop_iterate_one_value():
    """Ensure that the for loop iterator returns a single value."""
    expected_powers_list = [(0, 2 ** 0)]
    powers_list = iterate.calculate_powers_of_two_for_loop(0, 1)
    assert len(powers_list) == 1
    assert expected_powers_list == powers_list


def test_for_loop_iterate_five_value():
    """Ensure that the for loop iterator returns a single value."""
    expected_powers_list = [
        (0, 2 ** 0),
        (1, 2 ** 1),
        (2, 2 ** 2),
        (3, 2 ** 3),
        (4, 2 ** 4),
    ]
    powers_list = iterate.calculate_powers_of_two_for_loop(0, 5)
    assert len(powers_list) == 5
    assert expected_powers_list == powers_list


def test_for_loop_iterate_five_value_start_one():
    """Ensure that the for loop iterator returns a single value."""
    expected_powers_list = [(1, 2 ** 1), (2, 2 ** 2), (3, 2 ** 3), (4, 2 ** 4)]
    powers_list = iterate.calculate_powers_of_two_for_loop(1, 5)
    assert len(powers_list) == 4
    assert expected_powers_list == powers_list


def test_while_loop_iterate_one_value():
    """Ensure that the for loop iterator returns a single value."""
    expected_powers_list = [(0, 2 ** 0)]
    powers_list = iterate.calculate_powers_of_two_while_loop(0, 1)
    assert len(powers_list) == 1
    assert expected_powers_list == powers_list


def test_while_loop_iterate_five_value():
    """Ensure that the for loop iterator returns a single value."""
    expected_powers_list = [
        (0, 2 ** 0),
        (1, 2 ** 1),
        (2, 2 ** 2),
        (3, 2 ** 3),
        (4, 2 ** 4),
    ]
    powers_list = iterate.calculate_powers_of_two_while_loop(0, 5)
    assert len(powers_list) == 5
    assert expected_powers_list == powers_list


def test_while_loop_iterate_five_value_start_one():
    """Ensure that the for loop iterator returns a single value."""
    expected_powers_list = [(1, 2 ** 1), (2, 2 ** 2), (3, 2 ** 3), (4, 2 ** 4)]
    powers_list = iterate.calculate_powers_of_two_while_loop(1, 5)
    assert len(powers_list) == 4
    assert expected_powers_list == powers_list
