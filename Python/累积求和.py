count = 0  # 统计整数个数
total = 0   # 统计整数总和

while True:
    user_input = input().strip()  # 读取输入并去除首尾空格
    if user_input == '#':
        break  # 输入#时退出循环
    try:
        num = int(user_input)     # 尝试将输入转为整数
        count += 1
        total += num
    except ValueError:
        # 若输入非#且非整数，忽略该输入（按题目要求仅处理整数）
        continue

print(f"{count} {total}")