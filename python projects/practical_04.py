#present marks often by student input the value and get are division as the follows

mark=float(input("enter the student marks"))
if mark>=60:
    division="first division"
elif mark>=50:
    division="second division"
elif mark>=40:
    division="third division"
else:
    division="fail"
print("****student division****")
print(f"student division: {division}")
