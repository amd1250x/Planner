'''
specialTask.py - This file is for functions that are more unqiue than the
functions in basicTask.py. Most of these functions were written off the
top of my head, so some obvious omptimization may very well be needed
'''

# Once again, import basics, and datetime
from basicTask import *
import datetime

# This function takes a month and day param, both the numerical equivalencies (1/21 == January 21)
def getDayOfYear(m, d):
	# Created the months. They don't need to be populated, we just need the lengths
	Jan = list(range(31))
	Feb = list(range(28))
	Mar = list(range(31))
	Apr = list(range(30))
	May = list(range(31))
	Jun = list(range(30))
	Jul = list(range(31))
	Aug = list(range(31))
	Sep = list(range(30))
	Oct = list(range(31))	
	Nov = list(range(30))
	Dec = list(range(31))
	year = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
	totaldays = 365
	# Just so that we don't need to keep modifying them to ints
	imonth = int(m)
	iday = int(d)
	
	# If the year is not January...
	if year[imonth-1] > 0:
		# Set the total days to 0
		days = 0
		# Iterate through to get the days for each month preceding imonth, and add their lengths to days
		for i in range(imonth-1):
			days += len(year[i])
		# Add iday, the day from the param, to the total days
		days += iday
		return days
	else:
		# If it is January, The day in the year == the day in mm/dd form (Ex. January 23 is also the 23rd day of the year)
		return iday

# Simple function using datetime to get the current mm/dd
def getCurMonthDay():
	curMonth = int(time.strftime("%m"))
	curDay   = int(time.strftime("%d"))
	
	return [curMonth, curDay]

# This simply returns the number of days from today, until the day specified in dd and md
def getDaysUntilDue(dd, md):
	mdlist = getCurMonthDay()
	mddue = getDayOfYear(dd, md)
	mdtoday = getDayOfYear(mdlist[0], mdlist[1])
	return mddue-mdtoday


		
