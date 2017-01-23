def is_isogram(word):
    if not isinstance(word, basestring):
      raise TypeError("Argument should be a string")
    elif len(word) < 1 or word == "":
        return (word, False)
    else:
      for cha in word:
          if word.count(cha) > 1:
              return (word, False)
          else:
            return (word, True)
    return (word, True)

print is_isogram('11')
