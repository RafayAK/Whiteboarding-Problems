def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, likr "D6" and "B7":

        >>> check("D6", "H6")
        True

        >>> check("E6", "E4")
        True

        >>> check("B7", "D5")
        True

        >>> check("A1", "H8")
        True

        >>> check("A8", "H1")
        True

        >>> check("D6", "H7")
        False

        >>> check("E6", "F4")
        False

    """
    board = {'A': 8,
             'B': 7,
             'C': 6,
             'D': 5,
             'E': 4,
             'F': 3,
             'G': 2,
             'H': 1}

    if queen[0] == king[0] or queen[1] == king[1]:
        return True
    elif abs(int(king[1]) - int(queen[1])) == abs(board[king[0]] - board[queen[0]]) or abs(int(king[1]) + int(queen[1])) == abs(board[king[0]] - board[queen[0]]):
        return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
