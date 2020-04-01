first_name = "Kaitlyn"
last_name = "Ning"

def password_generator(first_name, last_name):
  #len() comes in handy when we are trying to select the last character in a string 
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)

print(temp_password)


'''
# Slice using len()
lyning

'''
