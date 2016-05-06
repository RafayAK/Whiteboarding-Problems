def spiral_matrix_print(m):
    """Given a 2D array prints all items of array

    in spiral order starting with the top left corner.

        >>> spiral_matrix_print([[11, 12, 13, 14, 15],[21, 22, 23, 24, 25],[31, 32, 33, 34, 35],[41, 42, 43, 44, 45]])
        11
        12
        13
        14
        15
        25
        35
        45
        44
        43
        42
        41
        31
        21
        22
        23
        24
        34
        33
        32

    """

    # calculate x and y limits
    y_limit = len(m)
    x_limit = len(m[0]) - 1

    # keep track of data already visited
    seen = set()

    # set up strating point
    x = 0
    y = 0

    print m[y][x]
    seen.add(m[y][x])

    # algorithm for traversing the matrix

    while len(seen) != len(m) * len(m[0]):
        # go right
        for step in range(x_limit):
            x += 1
            if m[y][x] not in seen:
                print m[y][x]
                seen.add(m[y][x])
        y_limit -= 1
        # go down
        for step in range(y_limit):
            y += 1
            if m[y][x] not in seen:
                print m[y][x]
                seen.add(m[y][x])
        # # go left
        for step in range(x_limit):
            x -= 1
            if m[y][x] not in seen:
                print m[y][x]
                seen.add(m[y][x])
        y_limit -= 1
        # go up
        for step in range(y_limit):
            y -= 1
            if m[y][x] not in seen:
                print m[y][x]
                seen.add(m[y][x])
        x_limit -= 1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
