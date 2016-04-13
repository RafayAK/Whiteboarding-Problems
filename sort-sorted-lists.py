# Given two already-sorted lists,
# write a function that returns a new list,
# that is the sorted merge of both of them.


def sort_ab(a, b):
    """Given already-sorted lists, 'a' and 'b', return sorted list of both.

    You may not use sorted() or .sort().

        >>> sort_ab(a = [1, 3, 5, 7], b = [2, 6, 8, 10])
        [1, 2, 3, 5, 6, 7, 8, 10]

    """
    result = []

    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    return result + a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
