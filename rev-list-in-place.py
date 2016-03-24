# Reverse a list in-place.


def rev_list_in_place(lst):
    """Reverse list in place, do not use reversed(), .reverse(), or list slice assignment.

        >>> rev_list_in_place([1, 2, 3])
        [3, 2, 1]

        """

    for i in range(len(lst) / 2):
        temp = lst[i]
        lst[i] = lst[-i - 1]
        lst[-i - 1] = temp

    # ALTERNATIVE:
    # for i in range(len(lst)/2):
    #    lst[i], lst[-i - 1] = lst[-i - 1], lst[i]

    return lst

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
