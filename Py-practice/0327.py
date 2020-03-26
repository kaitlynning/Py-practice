all_students = ["Alex", "Briana", "Kaitlyn", "Ken", "Dora", "Danny", "Josh", "Kitty", "Catherine", "Lisa"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
#add .pop() to take student off all_student list 
#add it to student_in_poetry list
  students_in_poetry.append(student)
#adding students use append 
print(students_in_poetry)
'''
# while
# Every time the condition of the while loop is satisfied, the code inside the while loop runs.

['Lisa', 'Catherine', 'Kitty', 'Josh', 'Danny', 'Dora']

'''
