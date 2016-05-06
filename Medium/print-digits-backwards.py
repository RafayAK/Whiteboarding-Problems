# Given an integer, print each digit in reverse order.
# For example, if you were given 1 you should simply print 1,
# if given 314 you should print 4, 1, 3, and if given 12 you should print 2, 1:


def print_digits(num):
    """Given int, print digits in reverse order.

        >>> print_digits(1)
        1

        >>> print_digits(314)
        4
        1
        3

        >>> print_digits(12)
        2
        1

    """
    lst = list(str(num))

    for i in range(len(lst)/ 2):
        lst[i], lst[- i - 1] = lst[- i - 1], lst[i]

    for digit in lst:
        print digit

# Runtime O(n^2)

    # Alternative solution, better runtime

    # while not num % 10 == num:

    #     next_digit = num % 10
    #     print next_digit
    #     num = (num - next_digit) / 10

    # print num

# Runtime O(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
