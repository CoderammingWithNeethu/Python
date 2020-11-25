name = input('Enter you name : ')
language=input('Enter which programming language you like ')

print('Hi {}! Let\'s get started with string formatting.'.format(name))

#TYPE 1 : by specifying the index of variables in format()
print('{0} likes to do programming in {1}'.format(name,language))
print('{1} programming.. {0} like to do.'.format(name,language))

#TYPE 2 : by default takes up index if not secified starting from 0, hence maintaining the order is important here
print('{} likes to do programming in {}'.format(name,language))

#TYPE 3 : by using keywords for the variables
print('{x} likes to do programming in {y}'.format(x=name,y=language))
print('{y} programming.. {x} like to do.'.format(x=name,y=language))

#TYPE 4 : For version of python 3.6+; by using f-string literal, directly mention variables in {}
print(f'{name} likes to do programming in {language}')
print(f'{language} programming.. {name} like to do.')
