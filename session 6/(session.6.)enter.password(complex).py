while True:
    password = input("enter password?")
    print(password)
    if password.isalpha():
        print("error")
    elif password.isdigit():
        print("error")
    else:
        print("your password is", password)
        break
