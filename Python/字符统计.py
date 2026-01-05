# 读取输入字符串
s = input()

# 初始化计数器
letters = 0  # 英文字符
spaces = 0   # 空格
digits = 0   # 数字
others = 0   # 其他字符

# 遍历字符串中的每个字符
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1

# 按格式输出结果
print(letters, spaces, digits, others)