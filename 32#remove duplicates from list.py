#remove duplicates from list
a=[1,2,3,6,8,7,4,5,1,9,8,3,18]
b=[]
for i in a:
    if i not in a:
        b.append(i)
print(b)