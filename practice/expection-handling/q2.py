age = int(input('Enter age: '))

if age<18:
    raise Exception('Age is invalid')
else:
    print('Age is valid')

