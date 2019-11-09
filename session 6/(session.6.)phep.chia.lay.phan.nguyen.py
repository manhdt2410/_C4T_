'''
    Ôn lại về phép chia lấy phần nguyên (dấu ‘//’).
    Điều gì sẽ xảy ra nếu ta lấy một số có 5 chữ số và dùng phép chia lấy phần nguyên số này cho 10?
     .Ví dụ: 124 // 10
'''

while True:
    n = input("enter a number")
    if len(n) < 5 or len(n) > 5:
        print("error")
    else:
        if n.isalpha():
            print("error")
        elif n.isdigit():
            print(int(n)//10)
            break
        else:
            print("error")
