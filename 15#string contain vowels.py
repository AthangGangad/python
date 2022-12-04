#string contain vowels
a=input("enter the sstring")
b=a.split("  ")
for i in b:
    for j in i:
        if(j==a or j==e  or j==i or j==o or j==u or j==A or j==I or j==O or j==U or j==E):
            print("string contain vowels:",j)
        else:
            print("string doesnot contain any vowels:",j)