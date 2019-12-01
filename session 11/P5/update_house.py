pc_shop = {
    "HP" : 20,
    "DELL" : 50,
    "MAC" : 12,
    "ASUS" : 30,
}
a = sum(pc_shop.values())
print("tong so may :", a)
b = int(input("so luong may da mua la :"))
print("so luong may con lai la :", a-b)