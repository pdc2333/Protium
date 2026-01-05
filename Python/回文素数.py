# 先处理输入，判断是否合法
n_input = input().strip()

# 检查输入是否为小数或负数
if '.' in n_input or n_input.startswith('-'):
    print("illegal input")
else:
    try:
        n = int(n_input)
        if n <= 1:
            print("illegal input")
        else:
            # 存储找到的回文素数
            result = []
            # 遍历2到n的所有数
            for num in range(2, n + 1):
                # 第一步：判断是否是素数
                is_prime = True
                if num == 2:
                    is_prime = True
                elif num % 2 == 0:
                    is_prime = False
                else:
                    # 检查从3到num的平方根是否能整除num
                    for i in range(3, int(num**0.5) + 1, 2):
                        if num % i == 0:
                            is_prime = False
                            break
                
                # 第二步：如果是素数，再判断是否是回文数
                if is_prime:
                    # 把数字转成字符串，判断是否和反转后的字符串相等
                    num_str = str(num)
                    if num_str == num_str[::-1]:
                        result.append(num_str)
            
            # 输出结果，用空格分隔
            print(' '.join(result))
    except:
        # 如果输入不是整数（比如字母），也输出非法
        print("illegal input")