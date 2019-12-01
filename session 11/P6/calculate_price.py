pc_shop = {
    "HP" : 20,
    "DELL" : 50,
    "MAC" : 12,
    "ASUS" : 30,  
    "ACER" : 25,  
}
pc_shop["TOSHIBA"] = 10
pc_shop["FUJITSU"] = 15
pc_shop["ALIENWARE"] = 5

pc_price = {
    "HP" : 600,
    "DELL" : 650,
    "MAC" : 12000,
    "ASUS" : 400,
    "ACER" : 300,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}
for i in pc_price:
    k = pc_shop[i] * pc_price[i]
    print(k)
for i in pc_price:
    print(i)
