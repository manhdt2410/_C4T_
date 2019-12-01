pc_shop = {
    "HP" : 20,
    "DELL" : 50,
    "MAC" : 12,
    "ASUS" : 30,
}
pc_shop["TOSHIBA"] = 10
for m,n in pc_shop.items():
    print(m,n,sep=':')
a = sum(pc_shop.values())
print(a)

print('\n')
pc_shop["FUJITSU"] = 15
pc_shop["ALIENWARE"] = 5
for m,n in pc_shop.items():
    print(m,n,sep=':')
print(a)