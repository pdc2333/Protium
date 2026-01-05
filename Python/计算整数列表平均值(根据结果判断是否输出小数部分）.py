a = eval(input())
total = sum(a)
if total%len(a) == 0:
    print(f"{total/len(a):.0f}")
else :
    print(f"{total/len(a):.2f}") 