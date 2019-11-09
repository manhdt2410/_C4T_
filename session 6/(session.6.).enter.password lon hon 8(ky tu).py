while True:
    password = input("enter password?")
    print(password)
    if len(password) <= 8:
         print("error")
    else:
        if password.isalpha():
            print("error")
        elif password.isdigit():
            print("your password is", password)
            break
        else:
            print("your password is", password)
            break
