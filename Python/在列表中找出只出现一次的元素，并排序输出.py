nums = eval(input())
a = []
for i in nums:
    if nums.count(i) == 1:
        a.append(i)
if a == []:
    print(False)
if a != []:
    a = sorted(a)
    b = ','.join(map(str,a))
    print(b)
'''   
#在最后的if之下可写成如下代码： 
    a.sort()
    print(*a,sep=',')
# * 的意思是解包列表，将列表中的每个元素作为单独的参数传递给print函数
'''