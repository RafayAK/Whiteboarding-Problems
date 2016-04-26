def group_anagrams(words):
    """
        >>> group_anagrams(["elvis", "softer", "god", "lives", "forest", "foster", "dog"])
        [['elvis', 'lives'], ['god', 'dog'], ['foster', 'softer', 'forest']]
    """
    def is_anagram(word1, word2):
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False

    result = []
    temp = []

    for word1 in words:
        temp.append(word1)
        for word2 in words:
            if is_anagram(word1, word2):
                if word2 not in temp:
                    temp.append(word2)
        for item in temp:
            words.remove(item)
        if temp:
            result.append(temp)
            temp = []

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
