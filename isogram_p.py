#Andela homestudy isogram challenge solution

def is_isogram(word):
    if not word:
      raise TypeError("Argument should be a string")
    
    if not len(word) > 1:
        return (word, False)

    for cha in word:
        if word.count(cha) > 1:
            return (word, False)
        else:
          return (word, True)
    return (word, True)

print is_isogram('Sample Isogram Word')
