string_nums = input("Enter a list of numbers, separated by ‘,’: ")
string_nums = string_nums.split(' ')
int_list =[]
for ch in string_nums:
    int_list.append(int(ch))
print ("int_list: ", int_list)
print("all even numbers :")
for i in list(int_list):
    if i % 2 == 0:
        print(i)
    else:
        continue