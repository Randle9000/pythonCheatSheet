from datetime import datetime, timedelta

start_date = '22/05/2020'
last_date = '26/05/2020'

start_date = datetime.strptime(start_date, '%d/%m/%Y')
last_date = datetime.strptime(last_date, '%d/%m/%Y')

print(last_date > start_date)
print(last_date < start_date)


while last_date >= start_date:
    print(start_date)
    start_date += timedelta(1)

    