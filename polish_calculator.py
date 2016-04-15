# Instead of writing 1 + 2 * 3, as we would in normal ("infix") style,
# we could write it with the operators to the left of their arguments.
# This expression would become + 1 * 2 3.


def calc(s):
    """Evaluate expression.

        >>> calc("+ 1 2")  # 1 + 2
        3

        >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
        6

        >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
        15

    """

    input_list = s.split(" ")

    num2 = int(input_list.pop())

    while input_list:

        num1 = int(input_list.pop())
        operator = input_list.pop()

        if operator == "+":
            num2 = num1 + num2
        elif operator == "-":
            num2 = num1 - num2
        elif operator == "*":
            num2 = num1 * num2
        else:
            num2 = num1 / num2

    return num2

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
