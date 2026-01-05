import math  # 用于计算平方根

def calc_f(x):
    # 根据分段条件计算函数值
    if x < 20:
        return 6 * (x ** 2) + 1
    elif 20 <= x < 40:
        return math.sqrt(3 * x - 60)
    else:  # x ≥ 40
        return 100 / (x + 1)

x = float(input())
result = calc_f(x)
print("{0:.2f}".format(result))