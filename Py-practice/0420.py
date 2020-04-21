def reverse_string(word):
  reverse = ""
 #you don’t want i to start at 0. Instead you want it to start at the last index of your string (len(my_string)-1) and end at 0 
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string("Kaitlyn"))

print(reverse_string("Hello!"))

print(reverse_string(""))

'''
nyltiaK
!olleH
'''
