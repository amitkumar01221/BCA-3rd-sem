#W.A.P using datetime module
from datetime import date,datetime
current=date.today()
print("current date:",current)
specific=date(2024,10,24)
print("specfic date",specific)
current_date=date.today()
year=current_date.year
month=current_date.month
day=current_date.day
print(f"year:{year},month:{month},day:{day}")
current_date=date.today()
format_date=current_date.strftime("%d/%m/%y")
print(f"formatted date:{format_date}")
p_datetime=datetime.strptime("27/10/2024 14:30:00","%d/%m/%Y %H %M %S")
print("full datetime:",p_datetime)