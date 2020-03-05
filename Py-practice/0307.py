#language list 
language = ['Chinese', 'English', 'Japanese']

#language tuple
language_tuple = ('Cantonese','Korean')

#language set
language_set = {'Spanish', 'German', 'French'}

#appending element of language tuple
language.extend(language_tuple)

print('Language List: ', language)

#extended language set
language.extend(language_set)

print('New Language List: ', language)

'''
Language List:  ['Chinese', 'English', 'Japanese', 'Cantonese', 'Korean']
New Language List:  ['Chinese', 'English', 'Japanese', 'Cantonese', 'Korean', 'French', 'German', 'Spanish']
'''