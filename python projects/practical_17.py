#exception handling using try , except and else
try:
    lst=[10,20,30,40]
    for num in lst:
        i=int(num)
        i=i*i
        print(i)
except NameError as args:
    print("nameerror",args)
else:
    print("total number procees",len(lst))
    del(lst)