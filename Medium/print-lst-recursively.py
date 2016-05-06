# Print items from a list using recursion.


def print_recursively(lst):
    """Print items in the list, using recursion.

        >>> print_recursively([1, 2, 3])
        1
        2
        3

    """

    if lst:
        print lst[0]
        return print_recursively(lst[1:])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
