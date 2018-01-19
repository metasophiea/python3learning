import numpy, pandas, datetime
from datetime import timedelta 








# imagine - if you will - that you're collecting values as time goes by
# It makes sense to store these values in a pandas' series with the timestamp
# Below, you can see this happen. We use the timestamp as the index
start = datetime.datetime(2017, 3, 31)
dates = [start - timedelta(days=x) for x in range(0, 10)]

values = [25, 50, 15, 67, 70, 9, 28, 30, 32, 12]
values2 = [32, 54, 18, 61, 72, 19, 21, 33, 29, 17]

ts1 = pandas.Series(values, index=dates)
ts2 = pandas.Series(values2, index=dates)

print(ts1)
print(ts2)
print( (ts1+ts2)/2 )
print()








# one can also create a range of dates using the following pandas' method
print( pandas.date_range('12/24/1970', '01/03/1971') )
print( pandas.date_range(start='12/24/1970', periods=4) )
print( pandas.date_range(  end='12/24/1970', periods=3) )
print( pandas.date_range('2017-04-07', '2017-04-13', freq="B") ) # here "B" means 'business days', thus only days that aren't on the weekend will be included
print( pandas.date_range('2016-02-25', '2016-07-02', freq="M") ) # this one will only return days that are at the end of a month
# these letters are called 'Aliases' here is the list:
#   B 	    business day frequency
#   C 	    custom business day frequency (experimental)
#   D 	    calendar day frequency
#   W 	    weekly frequency
#   M 	    month end frequency
#   BM 	    business month end frequency
#   MS 	    month start frequency
#   BMS 	business month start frequency
#   Q 	    quarter end frequency
#   BQ 	    business quarter endfrequency
#   QS 	    quarter start frequency
#   BQS 	business quarter start frequency
#   A 	    year end frequency
#   BA 	    business year end frequency
#   AS 	    year start frequency
#   BAS 	business year start frequency
#   H 	    hourly frequency
#   T 	    minutely frequency
#   S 	    secondly frequency
#   L 	    milliseonds
#   U 	    microseconds



