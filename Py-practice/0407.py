#str=word, single character x
def count_char_x(word, x):
  variable = 0
  for letter in word:
    if letter == x:
      variable += 1
  return variable

print(count_char_x("mississippi", "s"))

print(count_char_x("mississippi", "m"))

'''
4
1
'''
