high_score = [45, 67, 56, 78]
for i,a in enumerate(high_score):
    print(i+1, a)
new = int(input("enter your new high score :"))
high_score.append(new)
high_score.sort(reverse= True)
for i,a in enumerate(high_score):
    print(i+1, a)
