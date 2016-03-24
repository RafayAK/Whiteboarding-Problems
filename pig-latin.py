# Write a function to turn a phrase into Pig Latin.

# Your function will be given a phrase (of one or more space-separated words). There will be no punctuation in it.
# You should turn this into the same phrase in Pig Latin.

# Rules:

# 1. If the word begins with a consonant (not a, e, i, o, u), move the first letter to the end and add "ay".
# 2. If the word begins with a vowel, add "yay" to the end.


def pig_latin_word(string):
    """ For word in string if the word begins with a consonant (not a, e, i, o, u),
        move the first letter to the end and add "ay".
        If the word begins with a vowel, add "yay" to the end.
        Return new string.

        There will be no uppercase letters or punctuation in the phrase.


        >>> pig_latin_word('porcupine are cute')
        'orcupinepay areyay utecay'

        >>> pig_latin_word('give me an apple')
        'ivegay emay anyay appleyay'

        >>> pig_latin_word('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'

    """

    list_of_words = string.split()

    vowels = ["a", "e", "i", "o", "u"]

    result = []

    for word in list_of_words:
        if word[0] in vowels:
            result.append(word + "yay")
        else:
            word = word + word[0] + "ay"
            result.append(word[1:])
    return " ".join(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n)


# ALTERNATIVE SOLUTION:

# Helper function


# def pig_latin_word(word):
#     """Turn a word into the pig latin version.

#     For example::

#         >>> pig_latin_word('porcupine')
#         'orcupinepay'

#         >>> pig_latin_word('apple')
#         'appleyay'
#     """

#     if word[0] in 'aeiou':
#         return word + 'yay'

#     else:
#         return word[1:] + word[0] + 'ay'

# Main function


# def pig_latin(phrase):
#     """Turn a phrase into pig latin.

#     There will be no uppercase letters or punctuation in the phrase.

#         >>> pig_latin('hello awesome programmer')
#         'ellohay awesomeyay rogrammerpay'
#     """

#     # START SOLUTION

#     words = phrase.split(' ')

#     pl_words = [pig_latin_word(w) for w in words]

#     return " ".join(pl_words)
