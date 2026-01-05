OK = float(input())
if OK < 20 :
    q = OK**2*6+1
    print (f"{q:.2f}")
elif 20<=OK<40 :
    w = (3*OK-60)**(1/2)
    print (f"{w:.2f}")
elif OK>=40 :
    e = 100/(OK+1)
    print (f"{e:.2f}")