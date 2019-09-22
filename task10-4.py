def chop(list):
  del list[1]
  del list[-1]
t = [1, 2, 3, 4]
new_list = chop(t)
print(new_list)
