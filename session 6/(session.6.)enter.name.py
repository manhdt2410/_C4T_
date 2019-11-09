'''
Viết một chương trình yêu cầu người dùng nhập tên, nếu trong tên có chữ số, yêu cầu họ nhập lại
'''

while True:
    name = input("enter a name?")
    print(name)
    if name.isalpha():
        print("a name")
        print("your name is", name)
        break
    else:
        print("not a name")
