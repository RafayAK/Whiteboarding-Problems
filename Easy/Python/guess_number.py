"""
Guess number between 1 and 100
"""

def guess_number(number):
    too_low = 0
    too_high = 101
    guess = None
    while number != guess:
        guess = (too_high -too_low)/2 + too_low

        if guess > number:
            too_high = guess
        if guess < number:
            too_low = guess

