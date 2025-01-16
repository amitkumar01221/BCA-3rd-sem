def is_leap(year):
    leap=False
    for i in range(1900,100000):
        if (year%4==0 and year%100!=0) or (year %400==0):
            return True
        else:
            return False
    # Write your logic here
    return leap
year = int(input("enter the year"))
print(is_leap(year))