'''
Viết một chương trình yêu cầu người dùng nhập vào một số, đếm số chữ số của số vừa được nhập vào
Ví dụ:  Enter a number: 14680
 ==> The number you entered has 5 digits
'''

while True:
    number = input("enter a number")
    if number.isalpha():
        print("error")
    elif number.isdigit():
        print("the number you entered has", len(number), "digits")
        break
    else:
        print("error")
