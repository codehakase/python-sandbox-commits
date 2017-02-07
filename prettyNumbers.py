# Method to make numbers pretty
# 1000 -> 1.0K
# 1000000 -> 1.0M

from math import *

def get_shortened_integer(number_to_shorten):
    """ Takes integer and returns a formatted string """
    trailing_zeros = floor(log10(abs(number_to_shorten)))
    if trailing_zeros < 3:
        # Ignore everything below 1000
        return trailing_zeros
    elif 3 <= trailing_zeros <= 5:
        # Truncate thousands, e.g. 1.3k
        return str(round(number_to_shorten/(10**3), 1)) + 'k'
    elif 6 <= trailing_zeros <= 8:
        # Truncate millions like 3.2M
        return str(round(number_to_shorten/(10**6), 1)) + 'M'
    elif 9 <= trailing_zeros <= 10:
        # Truncate billions lik 1.2B
        return str(round(number_to_shorten / (10**9), 1)) + 'B'
    else:
        raise ValueError('Values larger or equal to a Trillion not supported')

print get_shortened_integer(1000000000)
