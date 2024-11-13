import math
a = input("enter a :")
b = input("enter b :")
c = input("enter c :")
d = (int ((b**2)) - (4*a*c))
print(d)
if d>0:
    x1=(((-b)+sqrt(d))/(2*a))
    x2=(((-b)-sqrt(d))/(2*a))
    print("there are two root %f and %f"(x1,x2))
elif d==0:
    x=(-b)/2*a
    print("there are onw root %f"(x))
else:
    print("no roots exsist")



    