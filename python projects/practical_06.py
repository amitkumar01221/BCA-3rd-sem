# Write a program call by value
def change(n):
    n[1]=n[1]+20
    print(n)
a=[10,20,30,40]
print(a)
change(a)
print(a)