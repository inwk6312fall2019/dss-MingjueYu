def has_duplicates(list):
  dictionary = dict()   
  for word in list:
    if word in dictionary:
      return True
    dictionary[word] = True
  return False
