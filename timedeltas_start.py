#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
# print(timedelta(days = 365, hours = 5, minutes = 1))

# print today's date
# now = datetime.now()
# print(str(now))

# print today's date one year from now
#  print(str(now + timedelta(days = 365)))

# create a timedelta that uses more than one argument
# print(str(now + timedelta(days = 3, weeks = 2, hours = 4)))

# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
today = date.day()
afd = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("April fools day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year +1)
# # Now calculate the amount of time until April Fool's Day  
time_to_afd = afd-today
print("it's just", time_to_afd, "days until the next april fools day")

