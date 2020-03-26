heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]


#by list comprehensions
can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

#by for loop
can_ride_coaster = []

for element in heights:
  if element > 161:
    can_ride_coaster.append(element)
print(can_ride_coaster)

'''
# compare function: list comprehensions and for loop
#list comprehension: convenient shorthand to create lists
[164, 170, 163, 163]
[164, 170, 163, 163]
'''
