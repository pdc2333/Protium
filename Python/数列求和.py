n = int(input())
if n == 0:
    print("0.0000")
else:
    sum_total = 0.0
    numerator = 2  # 第一项的分子
    denominator = 1  # 第一项的分母
    for _ in range(n):
        sum_total += numerator / denominator    # 更新分子和分母：新分子=原分子+原分母，新分母=原分子
        numerator, denominator = numerator + denominator, numerator
    print(f"{sum_total:.4f}")