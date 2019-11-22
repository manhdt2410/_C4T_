color_list = ["blue", "red", "teal", "green"]
pos = int(input("Enter position : "))
if pos == 1:
    print("color at position ", pos, ':', color_list[0])
elif pos == 2:
    print("color at position ", pos, ':', color_list[1])
elif pos == 3:
    print("color at position ", pos, ':', color_list[2])
elif pos == 4:
    print("color at position ", pos, ':', color_list[3])
else:
    print("invalid number!")
