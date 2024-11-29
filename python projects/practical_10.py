# write a program to use positional and keywords arguments:
def pro_arg(*args,**kwargs):
    print("positonal argument (*args)")
    for arg in args:
        print(arg)
        print("in keywords argument(**keargs):")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
pro_arg(1,2,3,name="SP",age=30,city="etawah");