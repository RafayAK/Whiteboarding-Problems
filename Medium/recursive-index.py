# Find the index of an item in a list using recursion.


def recursive_index(needle, haystack, i=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.
    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

        >>> recursive_index("hey", ["hey", "there", "you"])
        0

        >>> recursive_index("you", ["hey", "there", "you"])
        2

        >>> recursive_index("porcupine", ["hey", "there", "you"]) is None
        True

    """

    if i == len(haystack):
        return None
    else:
        if haystack[i] == needle:
            return i
        else:
            return recursive_index(needle, haystack, i + 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
