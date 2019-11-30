while True:
    print("How many legs an octopus has:")
    quiz = {
        "ans" : [3, 5, 2, 8],
        "moi" : "moi",
    }
    for n,m in enumerate(quiz["ans"]):
        print(n+1,m,sep=". ")
    ans = int(input("Your answer :"))
    if ans == 4 :
        print("Hura!!!")
        break
    else:
        print("Not a correct answer :( ")
