#write a program to handle standard exception 
try:
    x=int("not a number")
except ValueError as e:
    print("a value error occuored",e)
except TabError as e:
    print("a type error occured",e)
    