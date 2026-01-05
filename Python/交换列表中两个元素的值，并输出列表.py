a = input().split()
n,m = map(int,input().split())
a[n],a[m] = a[m],a[n]
print(a)