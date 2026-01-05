b = {}
while True :
    s = input().strip()
    if s == "q" :
        break
    b[s] = b.get(s,0) + 1
c = 0
d = ""
for e,f in b.items() :
    if f > c :
        c = f
        d = e
print(f"{d} {c}")