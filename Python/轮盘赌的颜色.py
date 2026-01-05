# 读取输入并转换为整数
try:
    num = int(input())
except:
    print("error")
else:
    # 判断输入范围
    if num < 0 or num > 36:
        print("error")
    elif num == 0:
        print("green")
    else:
        # 根据不同区间判断颜色
        if 1 <= num <= 10 or 19 <= num <= 28:
            if num % 2 == 1:
                print("red")
            else:
                print("black")
        elif 11 <= num <= 18 or 29 <= num <= 36:
            if num % 2 == 1:
                print("black")
            else:
                print("red")