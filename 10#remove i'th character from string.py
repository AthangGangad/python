#remove i'th character from string
a=input("enter the string")
b=int(input("enter the i'th value"))
c=b+1
d=a[:b]+a[c:]
print("the string is:",a,b,d)