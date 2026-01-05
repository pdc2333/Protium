import math

lis = eval(input())
lic = []
for i in lis :
    if i > 1:  # 素数大于1
        if i == 2:  # 2是素数
            lic.append(i)
        elif i % 2 != 0:  # 排除偶数
            is_prime = True
            max_div = math.isqrt(i)
            for j in range(3, max_div + 1, 2):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                lic.append(i)
print(lic)



##### 第一步：素数必须大于1，小于等于1的直接跳过
    #if num <= 1:
    #    continue
    
    # 第二步：假设当前数字是素数（先标记为True）
    #is_prime = True
    
    # 第三步：检查从2到num-1的数能不能整除num
    # 如果能整除，说明不是素数
    #for i in range(2, num):
    #    if num % i == 0:
    #        is_prime = False  # 标记为非素数
    #        break  # 找到一个因数就不用继续检查了
    
    # 第四步：如果最终还是素数，就添加到lic列表
    #if is_prime:
    #    lic.append(num)

    # 输出结果
    #print(lic)