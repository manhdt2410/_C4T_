name = input("enter your name : ")
while True:
    pw = input("enter password : ")
    cfpw = input("confirm password : ")
    if len(pw) > 8 and pw == cfpw :
        if pw.isalpha():
            print("error")
            continue
        elif pw.isdigit():
            print("error")
            continue
        else:
            print("OK!")
    else:
        print("invalid password!")
        continue
    email = input("enter your email : ")
    if "@gmail.com" not in email:
        print("invalid email!")
        continue
    else:
        break
print("Congratulation!", "\n", "Your account has been saved! ")
