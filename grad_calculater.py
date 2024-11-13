a=int(input("enter your marks a: "))
b=int(input("enter your marks b: "))
c=int(input("enter your marks c: "))
d=int(input("enter your marks d: "))
e=int(input("enter your marks e: "))

per=((a+b+c+d+e)/500)*100

if(per>90 and per<=100):
    print("A++")
elif(per>85):
    print("A+")
elif(per>75):
    print("A")
elif(per>70):
    print("B++")
elif(per>70):
    print("B+")
elif(per>60):
    print("B")
else:
    print("fail")
