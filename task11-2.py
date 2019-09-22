def invert_dict(dictionary):
  inverse = dict()
  for key in dictionary:
    value = dictionary[key]        
    inverse.setdefault(value, []).append(key)
  return inverse
