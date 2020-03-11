def calculate_age(current_year, birth_year):
	age = current_year - birth_year
	return age

my_age = calculate_age(2020, 1993)
dads_age = calculate_age(2020, 1960)

print("I am " + str(my_age) + " years old and my dad is "+ str(dads_age)+" years old" + ".")


'''
calculate_age

I am 27 years old and my dad is 60 years old.

'''