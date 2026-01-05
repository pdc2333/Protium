nums = eval(input())

# 使用字典统计每个数字出现的频率
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

# 找出最大的频率值（度）
degree = max(freq.values())
print(degree)