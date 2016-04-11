# Count the number of items in a list, using recursion.


def count_recursively(lst):
    """Return number of items in a list, using recursion.

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

    """

    if not lst:
        return 0

    else:
        return 1 + count_recursively(lst[1:])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
