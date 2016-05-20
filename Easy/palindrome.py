# Return True/False if this word is a palindrome.
# A palindrome is a word that is spelled the same backwards and forwards.


def is_palindrome(word):
    """Return True if word is palindrome, else return False.

        >>> is_palindrome("a")
        True

        >>> is_palindrome("noon")
        True

        >>> is_palindrome("racecar")
        True

        >>> is_palindrome("porcupine")
        False

        >>> is_palindrome("Racecar")
        False

    """

    i = 0
    j = -1

    while i < len(word)/2:
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
    
    # ALTERNATIVE SOLUTION
    
    # if word == word[::-1]:
    #     return True
    # else:
    #     return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
