import random
i = int(0)
d = str

while True:
    a = random.randint(1,100)
    b = random.randint(1,100)
    dau = random.randint(0,1)

    if dau == 0 :
        print(a,"+",b,"=")
        n = random.randint(0,1)
        if n == 0 :
            print(a + b)
            d =(input("answer ") )
            d = d.upper()
            if d == "T":
                i = i + 1
            elif d == "F":
                print("wrong answer!")
                break
            else:
                print("wrong input")
                break
        if n == 1 :
            print(random.randint(a + b - 2, a + b + 2))
            d = (str(input("answer ")))
            d = d.upper()
            if d == "T":
                print("wrong answer!")
                break
            elif d == "F":
                i = i + 1
            else:
                print("wrong input")
                break
    if  dau == 1 :
        print(a,"-",b,"=")
        m = random.randint(0,1)
        if m == 0 :
            print(a - b)
            d = (input("answer "))
            d = d.upper()
            if d == "T":
                i = i + 1
            elif d == "F":
                print("wrong answer!")
                break
            else:
                print("wrong input")
                break
        if m == 1 :
            print(random.randint(a - b + 2, a - b - 2))
            d = (input("answer "))
            d = d.upper()
            if d == "T":
                print("wrong answer!")
                break
            elif d == "F":
                i = i + 1
            else:
                print("wrong input")
                break
print("your score :", i)
