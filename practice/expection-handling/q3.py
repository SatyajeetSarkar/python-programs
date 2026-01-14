class auth_error(Exception):
    pass

password = '12345'
attempts = 0

while True:
    p = input('Enter passwword: ')
    try:
        if password == p:
            print('User logged in')
            break

        if attempts==2:
            raise auth_error
        
        attempts+=1
        print(f"Try again! {3-int(attempts)} attempts left !!")
    except auth_error:
        print('Too many attempts. User disabled!!')
        break