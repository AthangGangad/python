#function to check prime no or not
def prime(a):
    for i in range(2,a):
        if a%i==0:
            return "this is not prime number",a
        else:
            return "prime number",a
a=int(input("enter the number:"))
print(prime(a)) 