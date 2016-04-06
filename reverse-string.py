# Given a string, return the same string, reversed.
# For example, as "porcupine" would reverse to "enipucrop"


def rev_string(string):
    """Return reverse of string. You may NOT use the reversed() function or reverse() method.

        >>> rev_string("porcupine")
        'enipucrop'

    """
    result = ""

    for i in range(len(string)):
        result += string[-i - 1]

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
