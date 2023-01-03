from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

date1 = date.today()
print(date1)

date2 = date.today() + timedelta(days=8)
print(date2)

date3 = date.today() + timedelta(days=-365)
print(date3)

date4 = date3 + relativedelta(years=+8, months=+5, days=+9)
print(date4)
