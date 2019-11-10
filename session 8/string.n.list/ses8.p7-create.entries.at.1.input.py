name_string = input("name your things : ")
names = name_string.split(',')
print(names, '\n')
l = len(names)
print("your things :", '\n',)
for i in range(l):
    names[i] = names[i].upper()
    print(names[i], '\n')
