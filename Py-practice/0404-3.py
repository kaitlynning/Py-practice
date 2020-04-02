def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

print(letter_check("strawberry", "a"))
print(letter_check("orange", "a"))
print(letter_check("apple", "a"))
print(letter_check("kiwi", "a"))

'''

True
True
True
False

'''
