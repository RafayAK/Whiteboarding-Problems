def spiral_out(m):
    """ Given a square 2D array prints all items of array
    in spiral order starting from center and ending with the bottom right corner.

        >>> spiral_out([[11, 12, 13, 14, 15],[21, 22, 23, 24, 25],[31, 32, 33, 34, 35],[41, 42, 43, 44, 45],[51, 52, 53, 54, 55]])
        33
        34
        24
        23
        22
        32
        42
        43
        44
        45
        35
        25
        15
        14
        13
        12
        11
        21
        31
        41
        51
        52
        53
        54
        55

        >>> spiral_out([[11, 12, 13, 14],[21, 22, 23, 24],[31, 32, 33, 34],[41, 42, 43, 44]])
        23
        22
        32
        33
        34
        24
        14
        13
        12
        11
        21
        31
        41
        42
        43
        44

    """

    # find center/ starting point and print it out
    # depending on whether the length the side of the square is odd or even
    # select appropriate steps pattern
    if len(m) % 2 != 0:
        curr_y = len(m)/2
        curr_x = len(m)/2
        print m[curr_y][curr_x]
        odd_steps_pattern(len(m), m, curr_x, curr_y)
    else:
        curr_y = len(m)/2 - 1
        curr_x = len(m)/2
        print m[curr_y][curr_x]
        even_steps_pattern(len(m), m, curr_x, curr_y)

def odd_steps_pattern(len_matrix, matrix, x, y, i=1):
    """Pattern of steps for a square with an odd sides length:

        i = 1, i steps to the righht, i steps up, increment i
        i steps to the left, i steps down, increment the i

        repeat until i is equal length of the side.
    """

    if i == len_matrix:
        for steps in range(i - 1):
            x += 1
            print matrix[y][x]
    else:
        for steps in range(i):
            x += 1
            print matrix[y][x]
        for steps in range(i):
            y -= 1
            print matrix[y][x]

        i += 1
        if i < len_matrix:
            for steps in range(i):
                x -= 1
                print matrix[y][x]
            for steps in range(i):
                y += 1
                print matrix[y][x]
            i += 1
            return odd_steps_pattern(len_matrix, matrix, x, y, i)


def even_steps_pattern(len_matrix, matrix, x, y, i=1):
    """Pattern of steps for a square with an even sides length

        i = 1, i steps to the left, i steps down, increment i
        i steps to the right, i steps up, increment the i

        repeat until i is equal length of the side.

    """

    if i == len_matrix:
        for steps in range(i - 1):
            x += 1
            print matrix[y][x]
    else:
        for steps in range(i):
            x -= 1
            print matrix[y][x]
        for steps in range(i):
            y += 1
            print matrix[y][x]

        i += 1
        if i < len_matrix:
            for steps in range(i):
                x += 1
                print matrix[y][x]
            for steps in range(i):
                y -= 1
                print matrix[y][x]
            i += 1

        return even_steps_pattern(len_matrix, matrix, x, y, i)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
