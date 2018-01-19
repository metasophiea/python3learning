import datetime








# -- Date --
print(datetime.date.today())
print( str(datetime.date.today()) ) 
print(datetime.date.today().ctime()) # render as a C-style like string
print( datetime.date.today().day, '/', datetime.date.today().month, '/', datetime.date.today().year )
print(datetime.date.min)
print(datetime.date.max)
print( datetime.date(1993, 12, 14) )
print()

# the functions that follow can convert a date to/from the proleptic Gregorian ordinal
ord = datetime.date(1993, 12, 14).toordinal()
print( ord )
print( datetime.date.fromordinal(ord) )
print()

# get the weekday of this date
print( datetime.date(1993, 12, 14).weekday() ) # (it was a tuesday)
print()








# -- Time --
print( datetime.time.min )
print( datetime.time.max )
print( datetime.time(15,6,23) )
print( datetime.time(15,6,23).hour, ':', datetime.time(15,6,23).minute, ':', datetime.time(15,6,23).second )
print( datetime.time(15,6,23).replace(hour=11, minute=59) )
print()








# -- Difference --
# the act of finding the amount of time between different dates
delta = datetime.datetime(1993, 12, 14) - datetime.datetime(2017, 1, 31, 14, 17)
print( delta, ' -|' , delta.days, delta.seconds, '|- ', type(delta) )
print()
# adding/subtracting timedeltas
d1 = datetime.datetime(1991, 4, 30)
d2 = d1 + datetime.timedelta(10)
print(d1, ' - ', d2)
print(d2 - d1)
d3 = d1 - datetime.timedelta(100)
print(d3)
d4 = d1 - 2*datetime.timedelta(50)
print(d4)
print()
d1 = datetime.datetime(1991, 4, 30)
d2 = d1 + datetime.timedelta(10,100)
print(d1, ' - ', d2)
print(d2 - d1)








# -- Awareness --
# a date object being aware, means that it has information on what timezone it is in and whether day-light savings is a thing
# one can test if a date is aware like so
t = datetime.datetime(2017, 4, 19, 16, 31, 0)
print(t)

if t.tzinfo != None:
    if t.tzinfo.utcoffset(t) != None:
        print('obejct is aware')
# a datetime object must have both of these things

# one can create an aware object like so:
import pytz
t = datetime.datetime.now(pytz.utc)
print(t)
print( t.tzinfo, ' - ', t.tzinfo.utcoffset(t) )
print()








# strftime
# one can use this method to return a string representing the date and time, controlled by a format string
print(d1.strftime('%Y-%m-%d'))
print("weekday: " + d1.strftime('%a'))
print("weekday as a full name: " + d1.strftime('%A')) # Weekday as a decimal number, where 0 is Sunday and 6 is Saturday
print("weekday as a decimal number: " + d1.strftime('%w'))

print(d1.strftime('%d')) # Day of the month as a zero-padded decimal number. eg. 01, 02, ..., 31
print(d1.strftime('%b')) # Month as locale’s abbreviated name. eg. Jan, Feb, ..., Dec (en_US);  Jan, Feb, ..., Dez (de_DE)
print(d1.strftime('%B')) # Month as locale’s full name. eg. January, February, ..., December (en_US); Januar, Februar, ..., Dezember (de_DE)
print(d1.strftime('%m')) # Month as a zero-padded decimal number. eg. 01, 02, ..., 12
print()








# Phrasing
# this is the act of converting a string containing a date and/or time into a datetime object
# strptime
# this function uses a predefined format to extract the time from a string
print( datetime.datetime.strptime("30 Nov 00", "%d %b %y") )
print( datetime.datetime.strptime( "2007-03-04T21:08:12", "%Y-%m-%dT%H:%M:%S" ) )
print()

# we can go further with the dateutil module, which allows for automatic conversion without specifying a format
import dateutil.parser
print( dateutil.parser.parse('2011-01-03') )
print( dateutil.parser.parse('Wed Apr 12 20:29:53 CEST 2017') )