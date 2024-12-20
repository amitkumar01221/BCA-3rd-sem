list1=[]
element=int(input("Enter the number of element in the list"))
for i in range(element):
    item=int(input("enter the element"))
    list1.append(item)
print(list1)
# list convert to tuple
tuple1=tuple(list1)
print("the list convert to tuple")
print(tuple1)