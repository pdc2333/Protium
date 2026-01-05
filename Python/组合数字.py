# 读取输入并分割
input_line = input().strip()
parts = input_line.split()

# 第一步：检查输入是否为两个整数
if len(parts) != 2:
    print("illegal input")
else:
    try:
        n = int(parts[0])
        m = int(parts[1])
    except ValueError:
        print("illegal input")
    else:
        # 第二步：检查n < m是否成立
        if n >= m:
            print("illegal input")
        else:
            # 获取n到m（不含m）的所有数字，转为列表
            num_list = list(range(n, m))
            # 第三步：检查是否有至少3个数字
            if len(num_list) < 3:
                print("illegal input")
            else:
                # 新增：检查每个数字是否是0-9的有效数字（否则无法组成三位数）
                valid_digit = True
                for num in num_list:
                    if num < 0 or num > 9:
                        valid_digit = False
                        break
                if not valid_digit:
                    print("illegal input")
                else:
                    result = []
                    # 遍历所有可能的百位、十位、个位组合（确保数字不重复）
                    for i in range(len(num_list)):
                        for j in range(len(num_list)):
                            for k in range(len(num_list)):
                                # 三个位置的索引不能重复（保证数字不重复）
                                if i != j and j != k and i != k:
                                    hundreds = num_list[i]
                                    tens = num_list[j]
                                    units = num_list[k]
                                    # 百位不能为0（否则不是三位数）
                                    if hundreds != 0:
                                        three_digit = hundreds * 100 + tens * 10 + units
                                        result.append(str(three_digit))
                    # 第四步：检查是否有符合条件的数
                    if not result:
                        print("illegal input")
                    else:
                        print(' '.join(result))