
'''login system'''
users=[
    {"username":"shruti","password":"1234"},
    {"username":"admin","password":"pass"}

]
uname=input("enter username:")
pwd=input("enter password:")

for user in users:
    if user["username"]==uname and user["password"]==pwd:
        print("login successful")
        break
else:
    print("invalid")