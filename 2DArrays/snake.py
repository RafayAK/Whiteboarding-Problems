def snake(m):
    """ Given a square 2D array prints all items of array
    in snake order starting from top left corner.

        >>> snake([[11, 12, 13, 14, 15],[21, 22, 23, 24, 25],[31, 32, 33, 34, 35],[41, 42, 43, 44, 45],[51, 52, 53, 54, 55]])
        11
        12
        13
        14
        15
        25
        24
        23
        22
        21
        31
        32
        33
        34
        35
        45
        44
        43
        42
        41
        51
        52
        53
        54
        55

    """

    # set up strating point
    x = 0
    y = 0

    while y < len(m):
        try:
            for i in range(len(m[0])):
                print m[y][x]
                x += 1
            x -= 1
            y += 1
            for i in range(len(m[0])):
                print m[y][x]
                x -= 1
            x += 1
            y += 1
        except:
            return None


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
