import time
import calendar

# Tick is a second interval started in 0000 Jan 1 1970
ticks = time.time()
print ("Number of ticks since 12:00am, Jan 1, 1970:", ticks)

# TimeTuple
# Many time functions operate on tuple of 8 numbers
timeTuple = ('4-digit yr', 'month', 'day', 'hr', 'm', 's', 'day of week', 'Julian day of year (1~366)', 'daylight savings')

# It seems like time.time() is not quite necessary?
print(time.localtime(time.time()))


localtime = time.asctime(time.localtime(time.time()))
print (localtime)

# It's a tuple, so we can access the elements by the menas of [i]
curYr = time.localtime()[0]
curM = time.localtime()[1]
cal = calendar.month(curYr, curM)
print ("Here is the calendar for the current month:")
print (cal)