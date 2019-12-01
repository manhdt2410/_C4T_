pc_shop = {
    "HP" : 20,
    "DELL" : 50,
    "MAC" : 12,
    "ASUS" : 30,
}
a = input("hang may? ")
a = a.upper()
b = int(input("so luong? "))
print(pc_shop[a]-b)
