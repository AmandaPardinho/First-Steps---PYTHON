from datetime import datetime

currentDateAndTime = datetime.now()
print(currentDateAndTime)

formattedDate = currentDateAndTime.strftime('%d/%m/%Y')
print(formattedDate)

formattedTime = currentDateAndTime.strftime('%H:%M')
print(formattedTime)

