#max between 3 no
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print("the greater no is",a)
elif b>a and b>c:
    print("the greater no is",b)
else:
    print("greater no is",c)