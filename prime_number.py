# Write a function the returns True or False,
# depending on whether the integer passed into it is a prime number.


def is_prime(integer):
    """Return True if int is a prime number, else return False

        >>> is_prime(0)
        False

        >>> is_prime(1)
        False

        >>> is_prime(2)
        True

        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

        >>> is_prime(11)
        True

        >>> is_prime(999)
        False

    """

    if integer < 2:
        return False

    for n in range(2, integer):
        if integer % n == 0:
            return False

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
