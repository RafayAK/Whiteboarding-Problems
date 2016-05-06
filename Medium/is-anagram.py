# A palindrome is a word that reads the same forward and backwards (eg, "racecar", "tacocat").
# An anagram is a rescrambling of a word (eg for "racecar", you could rescramble this as "arceace").
# Determine if the given word is a re-scrambling of a palindrome.
# The word will only contain lowercase letters, a-z.
# Don't worry about whether it's an actual English word.
# For example, the word "bcbc" could be rearranged as "bccb", so this should be true.


def is_anagram_of_palindrome(string):
    """Determine if the given string is a re-scrambling of a palindrome.

        >>> is_anagram_of_palindrome("a")
        True

        >>> is_anagram_of_palindrome("ab")
        False

        >>> is_anagram_of_palindrome("aab")
        True

        >>> is_anagram_of_palindrome("arceace")
        True

        >>> is_anagram_of_palindrome("arceaceb")
        False

        >>> is_anagram_of_palindrome("aarceaceba")
        False

    """

    # count each letter

    counter = {}

    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    odd = 0

    for count in counter.values():
        if count % 2 != 0:
            odd += 1

    if odd == 0 or odd == 1:
        return True
    else:
        return False

# Alternative solution for lines 42-51

# seen_an_odd = False

#     for count in seen.values():
#         if count % 2 != 0:
#             if seen_an_odd:
#                 return False
#             seen_an_odd = True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)
