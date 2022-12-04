#check for armstrong or not
n=int(input("enter the no"))
s=0
n1=n
while n>0:
    d=n%10
    s=s+d**3
    n=n1//10
if s==n1:
    print("no is armstrong",n1)
else:
    print("no is not armstrong",n1)