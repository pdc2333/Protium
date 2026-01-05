name = input().split(',')
scores = eval(input())
result = [[name,scores] for name, scores in zip(name,scores)]
print(result)