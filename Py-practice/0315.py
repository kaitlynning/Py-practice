def graduation_reqs(gpa: float, credits: int):

  if (gpa >= 3.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 3.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 3.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (gpa < 3.0) and (credits < 120):
    return "You do not meet either requirement to graduate!"

'''
print(graduation_reqs(3.51234, 120))
You meet the requirements to graduate!

print(graduation_reqs(2.541, 120))
Your GPA is not high enough to graduate.

print(graduation_reqs(3.53, 100))
You do not have enough credits to graduate.

'''