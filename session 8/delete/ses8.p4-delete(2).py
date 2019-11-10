import random
list_0 = ['games', 'EXO', 'TV', 'Sports', 'LOL', 'BTS']
a = random.choices(list_0, k = 4)
print(a, '\n')
i = int(0)
while i < len(a):
    if a[i] == 'LOL' :
        a.remove('LOL')
        print(a, '\n', "had removed 'LOL'! ")
        break
    else:
        print(a)
        print("do not found 'LOL'! ") 
        break   
