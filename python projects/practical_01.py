 # write a program swap to number without use third arthmetic value
#user input value
a=int(input("enter the a value"))
b=int(input("enter the b value"))
print("****before swap*****")
print("a value is",a)
print("b value is",b)
#swaping using xor method
a=a^b
b=a^b
a=a^b
print("****after swaping****")
print("a value is",a)
print("b value is",b)

