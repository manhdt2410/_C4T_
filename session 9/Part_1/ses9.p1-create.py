color_list = ["blue", "red", "teal", "green"]
print("Our color list :")
print(*color_list,sep=', ')
new_color = input("Enter a new color : ")
color_list.append(new_color)
print("Our new coloe list : ") 
print(*color_list,sep=', ')
