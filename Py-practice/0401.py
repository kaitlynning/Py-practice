def odd_indices(lst):
  new_lst = []
#range(start, stop, step步長)
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

#list comprehension
def odd_indices(lst):
  new_list = [lst[i] for i in range(len(lst)) if i % 2 == 1]
  return new_list

#slice list 
  lst[1::2]
  lst[::2]

print(odd_indices([4, 3, 7, 10, 11, -2]))



'''
# odd indices 奇數位 
[3, 10, -2]

'''
