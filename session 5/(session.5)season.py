n = int(input("month in a year?"))
if n > 12 or n < 1:
    print("this month does not exist")
while 1 <= n <= 12:
    if n < 4:
        print("spring")
        break
    elif 3 < n < 7:
        print("summer")
        break
    elif 6 < n < 10:
        print("autumn")
        break
    else:
        print("winter")
        break
print("bye")
