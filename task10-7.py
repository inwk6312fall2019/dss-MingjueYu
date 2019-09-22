def has_duplicates(list):
	new_list = list.sort()
	for i in range(len(list) - 1):
		if new_list[i] == new_list[i+1]:
			return True
	return False
list = ['a', 'b', 'b']
print(has_duplicates(list))
