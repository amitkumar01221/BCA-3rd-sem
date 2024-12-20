lst=[h for h in range(1,12)]
lst2=[2,4,3,5,6,7,9,6]
l=[2,4,3,5,6,7]
l1=[2,4,3,6,7]
#del use that works on index num
print("del in list")
del lst2[2]
print(lst2)
# slicing technique for delete multiply items
print("slicing delete")
del lst2[2:]
print(lst2)
d=l.pop(3)
print("deleted element",d)
print(l)
# use only pop() whout pass any value on fun
print("whiout pass value in function")
d=l.pop()
print("deleted element",d)
print(l)
#use of remove that works on value
print("use remove fun")
l1.remove(2)
print(l1)
#use clear() all value delete or blank list
print("all value delete ")
lst.clear()
print(lst)