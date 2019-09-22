def nested_sum(list):
  result = 0
  for element in list:
    result = result + sum(element)
  return result
t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
