tenquan = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
sodan = ['150300', '247100', '333300', '266800', '420900', '318000']
for i in range(0, len(sodan)):
    sodan[i] = int(sodan[i])
b = sodan[0]
for i in sodan:
    if b < i:
        b = i
    else:
        continue
print(tenquan[sodan.index(b)],', so dan cua quan la',b)
c = sodan[0]
for x in sodan:
    if c > x:
        c = x
    else:
        continue
print(tenquan[sodan.index(c)],', so dan cua quan la',c)
