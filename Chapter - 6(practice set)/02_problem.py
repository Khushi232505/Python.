username = input("enter the username: ")
password = input("enter the password: ")

if (username == "admin" and password == "pass") :
    print("you have sucessfully loggedin")
elif (username != "admin"):
    print("wrong username")
else :
    print("wrong password")
