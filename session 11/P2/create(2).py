pc_shop = {
    "HP" : 20,
    "DELL" : 50,
    "MAC" : 12,
    "ASUS" : 30,
}
print(pc_shop)
a = input("ten hang may tinh :") 
a = a.upper()
b = int(input("so may : "))
pc_shop[a] = b
print(pc_shop)
