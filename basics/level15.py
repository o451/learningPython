import datetime
import calendar
for i in range(1006,1996,10) :
    d = datetime.date(i, 1, 27)

    if calendar.isleap(i) and d.weekday()==1:
        print(i)
