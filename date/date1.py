from datetime import date

currentDate = date.today()
print(currentDate)

dateInText = '{}/{}/{}'.format(currentDate.day, currentDate.month, currentDate.year)
print(dateInText)
