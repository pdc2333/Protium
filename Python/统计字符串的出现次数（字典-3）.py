a = list(input().split(" "))
b = {}
for i in a :
    b[i] = b.get(i,0) + 1
c = max(b.values())
e = sorted([i for i,t in b.items() if t == c])
for v in e :
    print(f"{v} {c}")