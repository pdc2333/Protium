n = int(input())
# 用字典存储伴侣关系（双向映射）
couple = {}
for _ in range(n):
    id1, id2 = input().split()
    couple[id1] = id2
    couple[id2] = id1
# 读取参加派对的人数M和客人ID列表
m = int(input())
guests = input().split()
# 用集合存储所有客人ID，方便快速查找
guest_set = set(guests)
# 收集落单的客人
single = []
for guest in guests:
    # 如果客人没有伴侣，或伴侣不在派对中，则落单
    if guest not in couple or couple[guest] not in guest_set:
        single.append(guest)
# 去重（因为客人列表可能重复，但题目保证输入无重复，可省略）
single = list(set(single))
# 按ID递增排序
single.sort()
# 输出结果
print(len(single))
if single:
    print(' '.join(single))