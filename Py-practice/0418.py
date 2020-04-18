def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)
# prints ["m", " ", "ippi"], len(word) = 3
print(count_multi_char_x("mississippi", "iss"))
#  print 2
print(count_multi_char_x("apple", "pp"))
#  print 1

'''
2
1
'''
