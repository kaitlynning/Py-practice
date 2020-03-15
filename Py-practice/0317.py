def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

'''
Control Flow review
Boolean expressions are statements that can be either True or False
A boolean variable is a variable that is set to either True or False.
You can create boolean expressions using relational operators:
Equals: ==
Not equals: !=
Greater than: >
Greater than or equal to: >=
Less than: <
Less than or equal to: <=
'''
