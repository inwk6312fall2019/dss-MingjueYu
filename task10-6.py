def is_anagram(text1, text2):
	text1.sort()
	text2.sort()
	return text1 == text2
text1 = ['k', 'e' ,'y']
text2 = ['y', 'e', 'k']
print(is_anagram(text1, text2))
