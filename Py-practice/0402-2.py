def max_num(nums):
  # Initializes the variable to the first value in the list
  maximum = nums[0]
  # Iterate over the list
  for number in nums:
  # Replace the value with current number. Maximum is growing in value. At the end of iteration, maximum will be the greatest value found in the list. There may be duplicates, but this method won’t be able to tell us that.
    if number > maximum:
      number = maximum
  return maximum
 
print(max_num([50, -10, 0, 75, 20]))


'''
# max num
75

'''
