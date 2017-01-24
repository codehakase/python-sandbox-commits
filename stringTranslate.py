import string
# Translate a pattern of strings to form a meaniful group of sentences

caption = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

new_string = ""

for letter in caption:
    found_pos = string.ascii_lowercase.find(letter)

    if found_pos == -1:
        new_string += letter
        continue

    index = found_pos + 2

    if index >= 26:
        index -= 26

    new_string += string.ascii_lowercase[index]

print maketrans(new_string)
