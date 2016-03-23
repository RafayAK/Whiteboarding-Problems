# Find the largest integer in a list of integers.


def max_num(num_list):
    """Returns largest integer from given list

        >>> max_num([5, 3, 6, 2, 1])
        6

    """
    max_number = num_list[0]

    for item in num_list:
        if item > max_number:
            max_number = item

    return max_number

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
