# Write a function that takes a list of numbers from 1 to max_num (inclusive),
# where 1 of the numbers is missing,
# as well as the max_num, and it should return the missing number.


def missing_number(lst, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *lst*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

        >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
        8

    """

    for num in range(1, max_num + 1):
        if num not in lst:
            return num

    raise Exception("None are missing!")

    # Alternative solution: find missing number by comparing expected sum vs actual

    # expected = sum(range(max_num + 1))

    # Alternatively, there's a math formula that finds the sum of 1..n
    # https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
    #
    # expected = ( n + 1 ) * ( n / 2 )
    #
    # This makes this problem O(1) !

    # return expected - sum(nums)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
