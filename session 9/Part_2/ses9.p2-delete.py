colors = ['blue', 'red', 'teal', 'green']
print("Our color list :")
for i,color in enumerate(colors) :
    print(i + 1, '.', color)


while True :
    if len(colors) > 0:
        a = input("color to delete : ")  
        if a.isdigit():  
            if a == '1' :
                colors.pop(0)
                for i,color in enumerate(colors) :
                    print(i + 1, '.', color)
            elif a == '2' :
                colors.pop(1)
                for i,color in enumerate(colors) :
                    print(i + 1, '.', color)
            elif  a == '3' :
                colors.pop(2)
                for i,color in enumerate(colors) :
                    print(i + 1, '.', color)
            elif a == '4' :
                colors.pop(3)
                for i,color in enumerate(colors) :
                    print(i + 1, '.', color)
            else :
                print("invalid number!")
        elif a.isalpha():
            if a in list(colors) :
                colors.remove(a)
                for i,color in enumerate(colors) :
                    print(i + 1, '.', color)
            else:
                print("fuck")
        else :
            print("invalid syntax")  
    else:
        print("Finish! no color left :v");
        break
