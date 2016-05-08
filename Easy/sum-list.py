# Compute the sum of a list of numbers.


def sum_list(num_list):
    """Return the sum of all numbers in list.

        >>> sum_list([5, 3, 6, 2, 1])
        17

        >>> sum_list([])
        0

    """

    sum_of_nums = 0

    for num in num_list:
        sum_of_nums += num

    return sum_of_nums
    
    # ALTERNATIVE SOLUTION
    
    # return sum(x for x in num_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
