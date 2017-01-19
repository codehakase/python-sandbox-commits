# function to check if a word is an isogram

def is_isogram(word):

    if not isinstance(word, basestring):
      raise TypeError("Argument should be a string")
    elif len(word) < 1:
        return (word, False)
    else:
        word = word.lower()

    for cha in word:
        if word.count(cha) > 1:
            return (word, False)
    return (word, True)

def user_input():
    print "Hello, this is a simple test to test for words that are isograms or not \n press enter to exit"
    print "======================================================================="
    print "======================================================================="
    entry = raw_input("Enter any word: ")
    if len(entry) < 1:
        verify = raw_input("are you sure you want to exist? Y/N ")
        if verify == "y" or verify == "Y":
            exist()
        elif verify == "n" or verify =="N":
            user_input()
    print is_isogram(entry)
    
    return user_input()

user_input()
