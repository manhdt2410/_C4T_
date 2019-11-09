email = input("enter your email ")
name = input("enter your name ")
pw = input("enter password ")
i = int(0)
while True:
    cfpw = input("confirm your password ")
    if pw != cfpw:
        print("error!")
    else:
        break
print("Congratulation!", "\n", "Your account has been saved! ")
