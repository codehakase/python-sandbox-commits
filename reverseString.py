# A function which takes a string as a parameter, reverses the string and returns it.

# Using iteration

import sys


def r_interation(word):
    reversedString = ''
    for i in range(1, len(word) + 1):
        reversedString += word[-i] # reversed
    return reversedString

# Using python's built in functions

def reverse_func(word):
    return "".join(reversed(word))

# using reversed slicing

def rev_slice(word):
    return word[::-1]

def main():
    param = sys.argv[1]
    print r_interation(param)
    print reverse_func(param)
    print rev_slice(param)

main()
