# nhập ngày tháng năm
y=input()
m=input()
d=input()

# ép kiểu số nguyên

y=int(y)
m=int(m)
d=int(d)



# kiểm tra xem năm có hợp lệ ko

if y <= 0:
    print("Invalid year")

# kiểm tra xem tháng có hợp lệ ko
else:
    if m < 1 or m > 12:
        print("Invalid month")
# set ngày max cho tháng
    else: 
        if m in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif m in [4, 6, 9, 11]:
            max_days = 30
        else: 
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                max_days = 29
            else: 
                max_days = 28
    if d<1 or d>max_days:
        print("Invalid date")
    else:
        print("Valid")

