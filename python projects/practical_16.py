# Write a program using exception handling to input 2 no
a=int(input("enter a value"))
b=int(input("enter b value"))
try:
    c=a/b
    print("result:",c)
except:
    print("can't devide by zero")
else:
    print("no exception execute successfully")