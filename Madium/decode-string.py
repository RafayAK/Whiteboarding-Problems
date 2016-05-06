# A valid code is a sequence of numbers and letters,
# always starting with a number and ending with letter(s).
# Each number tells you how many characters to skip before finding a good letter.
# After each good letter should come the next next number.
# For example, the string "hey" could be encoded by "0h1ae2bcy".
# This means "skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".


def decode(s):
    """Decode a string.

        >>> decode("0h")
        'h'

        >>> decode("2abh")
        'h'

        >>> decode("0h1ae2bcy")
        'hey'

    """
    result = ""

    for i in range(len(s)):
        if (s[i]).isdigit():
            counter = int(s[i])
            result += s[i + 1 + counter]

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
