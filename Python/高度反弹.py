a = float(input())
N = int(input())
if N == 1:
    print(f"{a}.2f")
else:
    b = a
    total = a
    for i in range(N-1):
        b = b*(1/2)
        total += 2*b
    print(f"{total:.2f}")