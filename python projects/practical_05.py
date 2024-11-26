# A list contain names of boys and girls as its elements boys name are started as tuple
#  WAP find out number of boys and girls in list
lst=["subh","nisha","suresh","radha",("raghav")]
boys=0
girls=0
for element in lst:
    if isinstance(element,type):
        boys+=1
    else:
        girls+=1
print("boys=",boys)
print("girls=",girls)