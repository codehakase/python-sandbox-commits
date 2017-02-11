from collections import OrderedDict
import collections

def remove_duplicates(word):
    unique_string = "".join(set(word))
    chars = "abcdefghijklmnopqrstuvwxyz"
    check_string = word

    for char in chars:
        count = check_string.count(char)
        if count > 1:
            return (unique_string, count)
        else:
            return (unique_string, count)

print remove_duplicates('thelexash')
