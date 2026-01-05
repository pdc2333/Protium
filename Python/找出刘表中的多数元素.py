def search(nums):
    dict1 = {}
    a = len(nums)
    for num in nums :
        dict1[num] = dict1.get(num,0)+1
    for key in dict1 :
        if dict1[key] > a//2 :
            return key
    return False
nums  =  eval(input())
y  =  search(nums)
print(y)