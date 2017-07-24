from account import login
from account import logout

data = raw_input("please enter your address:")

try:
    if data == 'login()':
        login()
    elif data == 'logout()':
        logout()

except Exception as e:
    print e
    print 'there is 404'
else:
    print 'correct'
finally:
    print 'execute the function anyway'
