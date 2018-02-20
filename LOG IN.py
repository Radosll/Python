passwords = ['1234', '0000', 'uktc', 'hello', 'abv']
names = ['Rado', 'Gogo', 'Niki']

myname = input('Enter name: ')
mypass = input('Enter password: ')
if (myname in names) & (mypass in passwords):


    print('Loged in')
else:
    print('Invalid log')