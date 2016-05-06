# Define a function max_of_three()
# that takes in three numbers as arguments and returns the largest of them.


def max_of_three(int1, int2, int3):
    """Return the largest number.

        >>> max_of_three(1, 5, 2)
        5

        >>> max_of_three(10, 1, 11)
        11
    """

    num_list = []

    num_list.append(int1)
    num_list.append(int2)
    num_list.append(int3)

    result = sorted(num_list)
    return result[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Runtime O(n logn)


# ALTERNATIVE SOLUTION:
#
# if num1 >= num2 and num1 >= num3:
#         return num1

#     elif num2 >= num1 and num2 >= num3:
#         return num2

#     elif num3 >= num2 and num3 >= num1:
#         return num3

#     else:
#         return "Something went wrong"
