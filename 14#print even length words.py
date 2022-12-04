#print even length words 
a=input("enter the string")
b=a.split(" ")
for i in b:
    if len(i)%2==0:
        print("word is even length",i)
    else:
        print("not even lengh string",i)