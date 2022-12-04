#no is prime or not
num=7
s=0
if num>1:
    for i in range(2,num):
        if(num%i==0):
            s=1
            break
if s:
    print("the given no is not a prime number",num)
else:
    print("the given no is prime",num)