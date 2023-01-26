attempts = 0

while attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "myusername" and password == "mypassword":
        print("Login successful!")
        break
    else:
        if username != "myusername" and password != "mypassword":
            print("Incorrect username and password.")
        elif username != "myusername":
            print("Incorrect username.")
        else:
            print("Incorrect password.")
    attempts += 1

if attempts == 3:
    print("Your account has been locked.")
