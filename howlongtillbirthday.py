from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today()
birthdate = date(2002, 10, 30)
birthday = date(today.year, 10, 30)
diffrence_birthdate = today-birthdate
print("your birthday was ",diffrence_birthdate , " ago")
if today > birthday:
    birthday = birthday.replace(today.year+1, 10, 30)
print("your birthday is in", birthday-today)

    

