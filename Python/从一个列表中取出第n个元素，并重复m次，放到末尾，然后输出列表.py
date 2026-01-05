a = list(map(int,input().split(',')))
n,m = map(int,input().split(","))
if n > len(a)-1 or n < -len(a) :
    print("error")
else :
    b = a[n]
    for i in range(m) :
        a.append(b)
    print(a)
