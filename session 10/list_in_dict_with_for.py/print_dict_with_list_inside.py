book = {
    "name" : "doraemon",
    "chars" : ["nobita", "doraemon", "shizuka"],
    "year" : 2000
}
book["country"] = "japan"
for k,v in book.items():
    print(k,v,sep='-')