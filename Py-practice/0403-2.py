first_name = "Angela"
last_name = "Baby"

def account_generator(first_name, last_name):
  account_name = first_name[:5] + last_name[:4]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)


'''
# Concatenating Strings

AngelBaby
'''
