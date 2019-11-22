num_list = ['12', '7', '3', '-31', '24']
i = int(0)
while True:
    num = input("Enter a number : ")
    if num not in list(num_list):
        print("number not in list!")
    elif num in list(num_list):
        pos = num_list.index(num)
        print("found, position ", pos + 1)
    else:
        print("invalid input!")

