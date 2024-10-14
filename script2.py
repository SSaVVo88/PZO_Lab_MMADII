from datetime import datetime

current_date = datetime.now()

formated_date = current_date.strftime("%A,%d %B %Y %H:%M:%S")
print(formated_date)