print("welcome to the user registration and login system")
user={}

 
while True:

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice=input("enter your choice:")
    if choice=="1":
        username=input("enter your username:")
        password= input("enter your password:")
        user[username]= password
        print("registrattion successufl")
    elif choice=="2":
        username= input("enter your username:")
        password= input("enter yout passsword:")
        if username in user and user[username]== password:
            print("login sucessful")
        else: print("invalid user name or password")
    elif choice=="3":
        print("exiting the program")
        break
    else: print("invalid choice")
