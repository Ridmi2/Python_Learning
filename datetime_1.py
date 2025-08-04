import datetime
#date(year ,month,date)
b_day = datetime.date(2012,4,12)
print(b_day)

today=datetime.date.today()
print(today)
print(today.isoweekday())#if weekday monday wil be represented in 0,if it is weekday monday will be represented as 0
print(b_day.strftime('%A, %B %d, %Y'))
age = today-b_day
print(age)


#time(hour,minutr,second,microsecond)
t=datetime.time(9,30,45,10000)
print(t)
print(t.hour)#only hour

#both time and date
t=datetime.datetime.today()
print(t)
print(t.time())

t_delta=datetime.timedelta(days=20)
print(t-t_delta)