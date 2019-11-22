high_score = [45, 67, 56, 78, 103, 88, 31]
new = int(input("enter your new high score :"))
high_score.append(new)
b = high_score.sort(reverse= True)
for i,a in enumerate(high_score):
    print(i+1, a)
    if i == 4:
        break

