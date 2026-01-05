a = input().split(",")
b = list(map(int,input().split(",")))
c = []
d = [[a1,b1] for a1,b1 in zip(a,b)]
e = sorted(d, key=lambda x: x[1])
print(e)