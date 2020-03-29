def exponents(bases, powers):
  new_lst = []
#takes two list 
  for base in bases:
    for power in powers:
# a ** b is a to the power of b
      new_lst.append(base ** power)
  return new_lst


print(exponents([2, 3, 4], [1, 2, 3]))


'''
# nested for loops
# The outer for loop should loop through all of the bases and the inner for loop should loop through all of the powers. 
[2, 4, 8, 3, 9, 27, 4, 16, 64]

'''
