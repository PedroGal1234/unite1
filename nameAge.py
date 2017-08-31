#Pedro Gallino
#8/31/17
#nameAge.py - how to tell how many letters are in a name and how old you will be next year

name = input('What is you name? ')
age = int(input('How old are you? '))
name1,name2 = name.split()
print('Your name has', len(name),'letters')
print('Your first name has',len(name1),'letters')
print('Your last name has',len(name2),'letters')
print('Next year you will be', age+1,'years old')
