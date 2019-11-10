this_list = ['games', 'LOL', 'BTS', 'study']
while True:
    d = ('C', 'R', 'U', 'D')
    d = str(input("choose a letter : "))
    d = d.upper()
    if d == 'C' :
        print(this_list)
        new_item = input("new item : ")
        this_list.append(new_item)
        print(this_list)
        break
    elif d == 'R' :
        l = len(this_list)
        for i in range(l) :
            print(this_list[i])
    elif d == 'U' :
        print(this_list)
        i = int(input("choose a number? "))
        if -4 < i < 4 :
            this_list[i] = input("enter your change? ")
            print(this_list)
        else:
            print("invalid number")
    else :
        print(this_list)
        i = int(input("type a number? "))
        if -4 < i < 4 :
            this_list.pop(i)
            print(this_list)
        else:
            print("error!!")
