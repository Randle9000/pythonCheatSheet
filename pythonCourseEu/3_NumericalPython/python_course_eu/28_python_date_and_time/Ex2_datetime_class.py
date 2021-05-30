
def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))

# datetime class
splitter('datetime class')
from datetime import datetime
# naive
t_1 = datetime(2016, 4, 12, 12, 33, 1)
print(t_1, '\n')
print('t_1.tzinfo, if None then naive else aware \n', t_1.tzinfo, '\n')

# aware
import pytz
t_3 = datetime.now(pytz.utc)
print(t_3, '\n')
print('t_3.tzinfo: \n', t_3.tzinfo, '\n')
print('t_3.tzinfo.utcoffset(t_3): \n', t_3.tzinfo.utcoffset(t_3), '\n')

#timedelat
from datetime import timedelta as delta
ndays = 15
start = datetime.now()
dates = [start - delta(days=x) for x in range(0, ndays)]
print(dates, '\n')
#for x in dates:
#    print(x)

delta = datetime.now() - datetime(2020, 8, 1)
print('delta :', delta, '\n\ndelta.days: ', delta.days, '\n') # it could be seconds etc.

# date time to string and to strftime
splitter('date time to string and to strftime')
s = str(start)
print('str(start)', s, '\n')
print("""start.strftime('%Y-%m-%d')""", '\n', start.strftime('%Y-%m-%d'), '\n')
print('start.strftime("%a)"), \n ', "weekday: " + start.strftime('%a'), '\n')
print('start.strftime("%A""): \n', "weekday as a full name: " + start.strftime('%A'), '\n')

# Weekday as a decimal number, where 0 is Sunday
# and 6 is Saturday
print("""start.strftime('%w')""", "\nweekday as a decimal number: " + start.strftime('%w'), '\n')


# creating time object from str
splitter('creating time object from str')
t = datetime.strptime("30 Nov 00", "%d %b %y")
print(t)

dt = "2007-03-04T21:08:12"
datetime.strptime( dt, "%Y-%m-%dT%H:%M:%S" )
print(dt)

dt = '12/24/1957 4:03:29 AM'
dt = datetime.strptime(dt, '%m/%d/%Y %I:%M:%S %p')
print(dt)

dt = 'Wed Apr 12 20:29:53 CEST 2017'
dt = datetime.strptime(dt, '%a %b %d %H:%M:%S %Z %Y')
print(dt)



from dateutil.parser import parse
parse('2011-01-03')
parse('Wed Apr 12 20:29:53 CEST 2017')




