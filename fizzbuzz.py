# Write a program that counts from 1 to 20 in fizzbuzz fashion.

# Loop from 1 to 20 (inclusive). Each time through,
# if the number is evenly divisible by 3, say "fizz"
# If the number is evenly divisible by 5, say "buzz".
# If the number is evenly divisible by both 3 and 5, say "fizzbuzz".
# Otherwise, say the number.


def fizzbuzz():
    """ Count from 1 to 20 in a fizzbuzz fashion.

        >>> fizzbuzz()
        1
        2
        fizz
        4
        buzz
        fizz
        7
        8
        fizz
        buzz
        11
        fizz
        13
        14
        fizzbuzz
        16
        17
        fizz
        19
        buzz

    """

    for num in range(1, 21):
        if num % 3 == 0 and num % 5 == 0:
            print "fizzbuzz"
        elif num % 3 == 0:
            print "fizz"
        elif num % 5 == 0:
            print "buzz"
        else:
            print num

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
