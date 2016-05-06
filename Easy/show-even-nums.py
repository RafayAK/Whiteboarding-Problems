# Given a list of integers, some even and some odd,
# write a function that returns the indices of all the numbers which are even.


def show_evens(lst):
    """Given list of ints, return list of *indices* of even numbers in list.

        >>> show_evens([1, 2, 3, 4, 6, 8])
        [1, 3, 4, 5]

        >>> show_evens([2, 4, 6, 8])
        [0, 1, 2, 3]

    """

    result = []

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            result.append(i)

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
