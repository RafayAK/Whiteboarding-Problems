# Write a function that works like built-in Python .split() method.
# You may not use the split method in your solution!
# You may not use regular expressions in your solution!

def split(astring, splitter):
    """Split astring by splitter and return list of splits.

        >>> split("i love balloonicorn", " ")
        ['i', 'love', 'balloonicorn']

        >>> split("that is which is that which is that", " that ")
        ['that is which is', 'which is that']

        >>> split("that is which is that which is that", "that")
        ['', ' is which is ', ' which is ', '']

        >>> split("hello world", "nope")
        ['hello world']

    """

    out = []
    start = 0

    for i in range(len(astring)):
        if astring[i] == splitter[0]:
            if astring[i: (i + len(splitter))] == splitter:
                out.append(astring[start: i])
                start = i + len(splitter)

    out.append(astring[start:])

    return out

    # Aleternative solution:

    # out = []
    # index = 0

    # while index <= len(astring):

    #     curr_index = index
    #     index = astring.find(splitter, index)

    #     if index != -1:
    #         out.append(astring[curr_index:index])
    #         index += len(splitter)

    #     else:
    #         # couldn't find any more instances of splitter in astring
    #         out.append(astring[curr_index:])
    #         break

    # return out


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
