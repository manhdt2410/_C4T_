pc_prices = {
    "HP" : 600,
    "DELL" : 650,
    "MAC" : 12000,
    "ASUS" : 400,
    "ACER" : 300,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}
a = input("name?")
a = a.upper()
print(pc_prices[a])