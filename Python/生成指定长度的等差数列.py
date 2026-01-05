a = list(map(int, input().split(',')))
d =[a[0]]
b =a[0]
while len(d)<a[1]:
    b += a[2]
    d.append(b)
print(d)