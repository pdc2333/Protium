# 读取输入的两个颜色
color1 = input().strip().lower()  # 转为小写，避免大小写问题
color2 = input().strip().lower()

# 定义原色集合
primary_colors = {'red', 'blue', 'yellow'}

# 判断是否是合法原色且不重复
if color1 not in primary_colors or color2 not in primary_colors or color1 == color2:
    print("error")
else:
    # 判断混合结果
    if {color1, color2} == {'red', 'blue'}:
        print("purple")
    elif {color1, color2} == {'red', 'yellow'}:
        print("orange")
    elif {color1, color2} == {'blue', 'yellow'}:
        print("green")