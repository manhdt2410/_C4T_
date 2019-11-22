ten_quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
danso_cua_quan = ['150300', '247100', '333300', '266800', '420900', '318000']
for i in range(0, len(danso_cua_quan)):
    danso_cua_quan[i] = int(danso_cua_quan[i])
a = max(danso_cua_quan)
b = min(danso_cua_quan)
print("so dan nhieu nhat la", a)
print("so dan it nhat la", b)
