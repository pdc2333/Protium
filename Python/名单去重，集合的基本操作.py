list1 = input().split(',')  #生成集合#
set1 = set(list1)

list2 = input().split(',')
set2 = set(list2)

intersection = list(set1 & set2)
union = list(set1 | set2)

print(intersection)
print(union)