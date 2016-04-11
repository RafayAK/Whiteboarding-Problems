#Given two lists. concatenate them
#(that is, combine them into a single list).


def concat_lists(list1, list2):
    """Combine two lists into a single list

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]

    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []

    """

    # same as list1 + list2
    # same as list1.extend(list2)

    for item in list2:
        list1.append(item)

    return list1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
