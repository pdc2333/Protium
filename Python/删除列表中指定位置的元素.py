a = eval(input())
n,m =map(int,input().split(","))
if n >= 0 and m <= len(a) and n<=m:
    del a[n:m]
    print(a)
else:
    print("error")
