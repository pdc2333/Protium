length = float(input())
width = float(input())

if length <= 0 or width <= 0:
    print("illegal data")
elif length == width:
    print("It's a square")
else:
    print("It's a rectangle")