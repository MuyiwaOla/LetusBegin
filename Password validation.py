import re
print('This is a password checker')
password = str(input('Please enter your password: '))

checker = re.search('[a-z]','[A-Z]', password)

if (checker):
    print('Your password passes the checks')
else:
    print('Make a new password')
    
