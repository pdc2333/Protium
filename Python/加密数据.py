s = input()
a = []
for c in s:
    num = int(c)
    b = num + 5
    c = b % 10
    a.append(c)
d = []
length = len(a)
for i in range(length):
    reversed_num = a[length - 1 - i]
    d.append(reversed_num)
result = ""
for num in d:
    result = result + str(num)
print(result)