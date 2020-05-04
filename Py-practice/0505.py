drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(drinks_to_caffeine)
#List Comprehensions to Dictionaries
#zip() combines two lists into a zipped list of pairs

'''
{'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}
'''
