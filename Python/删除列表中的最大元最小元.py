a = eval(input())
q = max(a)
w = min(a)
c = []
for num in a :
    if num != q and num != w :
        c.append(num)
print(c)