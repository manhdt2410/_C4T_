quiz = {
        "ans1" : [3, 5, 2, 8],
        "ans2" : [2, 5, 3, 4],
        "ques1" : "How many legs an octopus has :",
        "ques2" : "How many legs a dog has :"
    }
i = int(0)
d = int(0)
p = float
while True:
    print(quiz["ques1"])
    for n,m in enumerate(quiz["ans1"]):
        print(n+1,m,sep=". ")
    ans = int(input("Your answer :"))
    if ans == 4 :
        print("correct!")
        d = d + 1
        i = i + 1
        print("your score :", i)
        break
    else:
        print("Not a correct answer :( ")
        d = d + 1
        print("your score :", i)
        break
while True:
    print(quiz["ques2"])
    for n,m in enumerate(quiz["ans2"]):
        print(n+1,m,sep=". ")
    ans = int(input("Your answer :"))
    if ans == 4 :
        print("correct!")
        d = d + 1
        i = i + 1
        print("your score :", i)
        break
    else:
        print("Not a correct answer :( ")
        d = d + 1
        print("your score :", i)
        break
print('\n', "total score :", i)
p = (i/d)*100 
print("correct answer percentage : ", p, '%')