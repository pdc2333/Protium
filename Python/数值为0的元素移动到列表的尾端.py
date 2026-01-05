a = input().strip()
nums = [int(num) for num in a[1:-1].split(',')]
nozero = []
zeros = []
for num in nums:
    if num != 0:
        nozero.append(num)
    else:
        zeros.append(num)
result = nozero + zeros
print(result)