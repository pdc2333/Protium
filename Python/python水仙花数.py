start = int(input())
for num in range(100, start):
    if num < 1000:  
        continue
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    if hundreds**3 + tens**3 + ones**3 == num and num <= start :
        print(num)
    else:
        print("none")