import random 

def has_duplicates(t):#if there are classmates who have birthdays on the same day
  new_list = list(t)	
  new_list.sort()	
  for i in range(len(t) - 1):		
    if new_list[i] == new_list[i+1]:			
      return True	
  return False
  
def random_birthday(n):#Randomly generate 23 classmates' birthdays and save them as a list
	birthday_list = []
	for i in range(n):
		birthday = random.randint(1, 365)
		birthday_list.append(birthday)
	return birthday_list
