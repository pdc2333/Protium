a = list(input().split(" "))
name = a[0]
english = float(a[1])
python = int(a[2])
math = int(a[3])
total = english + math + python
avg = total / 3
b = [english, math, python]
b.sort()
b.reverse()
b.append(avg)
b = [f"{i:.2f}" for i in b]
print(name,*b)