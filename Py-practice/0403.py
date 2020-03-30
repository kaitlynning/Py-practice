def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
  # It is accessing the second list with an index that is the same distance from the right end as index is from the left.
  # len(lst2) - 1 from the right
  # len(lst2) - 1 - index from the left
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


'''
# Reversed list
True 
False

'''
