# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from datetime import  date

date1 = date(1901,1,1 )
date2 = date(2000,1,31)

date1_ord = date1.toordinal()
date2_ord = date2.toordinal()
cnt = 0

for d_ord in range(date1_ord, date2_ord):
    d = date.fromordinal(d_ord)
    if (d.weekday() == 6) and (d.day == 1):
        cnt = cnt + 1

print("Number of Sunday 1'st days is {}".format(cnt))
