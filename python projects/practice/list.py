#slicing
l=[2,3,4,5,6]
print(l[0:])
print(l[0:3])
print(l[0:5:2])
#indexing
print("indexing")
print(l[1])
#find the lenght of the list
print("find the lenght of the list")
print(len(l))
print("list iteration")
for i in l:
    print(i)
#second logic
print("second logic")
t=len(l)
for i in range(t):
    print(l[i])
#list comperision
print("list comparision")
lst2=[h for h in range(1,11)]
print(lst2)
d="hello every one"
output=[h for h in d]
print(output)