# Given list of ints, return True if any two nums in list sum to 0.

def add_to_zero(list_of_ints):
    """Return True if any two ints in a list add to zero else return False

        >>> add_to_zero([])
        False

        >>> add_to_zero([1])
        False

        >>> add_to_zero([1, 2, 3])
        False

        >>> add_to_zero([1, 2, 3, -2])
        True

    """
    if len(list_of_ints) == 0:
        return False
    else:
        for item in list_of_ints:
            if -item in list_of_ints:
                return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n**2)
