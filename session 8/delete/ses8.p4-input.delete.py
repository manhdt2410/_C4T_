list_0 = ['games', 'EXO', 'TV', 'Sports', 'LOL', 'BTS']
print(list_0)
i = int(input("type a number? "))
if -7 < i < 6:
    list_0.pop(i)
    print(list_0)
else:
    print("error!!")
