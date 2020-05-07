pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
#key, value = occupation, percentage
for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 

'''
Women make up 28 percent of CEOs.
Women make up 9 percent of Engineering Managers.
Women make up 58 percent of Pharmacists.
Women make up 40 percent of Physicians.
Women make up 37 percent of Lawyers.
Women make up 9 percent of Aerospace Engineers.

Each element of the dict_list returned by .items() is a tuple consisting of(key, value)
'''
