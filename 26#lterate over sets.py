#lterate over sets
a={1,2,"rbnb",(2,5,9,7),"sai","ram"}
print(a)
a.add(55)
a.update([5,8,7,2])
print(a)
a.discard("sai")
print(a)
a.remove(1)
print(a)
b={55,7,66,2,77,"ram"}
c=a.union(b)
print(c)