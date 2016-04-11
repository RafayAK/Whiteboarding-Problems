# Return n unique random numbers from 1-10 (inclusive).

# Given the numbers 1-10, return n random numbers,
# making sure to never return the same number twice.
# You can trust that this function will never be called with n < 0 or n > 10.

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).

        >>> len(lucky_numbers(2))
        2

        >>> lucky_numbers(0)
        []

        >>> sorted(lucky_numbers(10))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """
    possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lucky_nums = []

    for i in range(n):
        # select random number from possible_nums
        lucky_number = random.choice(possible_nums)
        # remove lucky_number from possible_nums
        possible_nums.remove(lucky_number)
        # append lucky_number to
        lucky_nums.append(lucky_number)

    return lucky_nums

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
