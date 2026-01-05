GDP = {}
while True :
    a = list(input().split(" "))
    if a[0] == "ok" :
        break
    GDP[a[0]] = int(a[1])
keys = list(GDP.keys())
values = list(GDP.values())
keys.sort()
values.sort()
if "India" in keys :
    b = "yes"
else :
    b = "no"
sum = sum(values)
print(keys,values,b,sum,sep="\n")