def raises_value_error():
  raise ValueError

try:
  raises_value_error()
  #function call
except ValueError:
  print("You raised a ValueError!")
  #error message

 '''
 control flow: try and except statement

 You raised a ValueError!
 
 '''
