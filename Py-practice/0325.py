dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)

  if dog_breed == dog_breed_I_want:
    print("They have the dog I'm looking for!")
    break

# Anything after break is unreachable.
    print("End of search!")

'''
# break

french_bulldog
dalmatian
They have the dog I'm looking for!

'''
