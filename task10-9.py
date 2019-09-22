def fuction_1():	
  file = open("words.txt")	
  l1 = []	
  for line in file:		
    word = line.strip()		
    l1.append(word)	
  return l1
  
def fuction_2():	
  file = open("words.txt")	
  l2 = []	
  for line in file:		
    word = line.strip()		
    l2 = l2 + [word]
  return l2
  
#How to compare time
