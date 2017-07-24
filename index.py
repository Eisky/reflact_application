from  account import login
from  account import logout
data = raw_input("please enter your address:")
array = data.split('/')
if data == 'login()':
    login()
elif data == 'logout()':
    logout()
else:
    print 'address is incorrect'
