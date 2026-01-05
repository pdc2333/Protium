a = eval(input())
a.sort(reverse=False)
c = 0
for i in range(0,len(a)) :
    c += a[i] * 10**i
print(c)
'''
a = eval(input())
b = sorted(a, reverse=True)
result = int(''.join(map(str, b)))
print(result)
'''