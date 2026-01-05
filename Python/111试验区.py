def  print_matrix(n):
    for i in range(1, n + 1):
        a = []
        for j in range(1, n + 1):
            a.append(str(min(i, j)))
        print(' '.join(a))
number=eval(input())
print_matrix(number)