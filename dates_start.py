#
# Example file for working with date information
#
from datetime import time
from datetime import date
from datetime import datetime
def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
 # today = date.today()
 # print ("todays date is " + str(today))

  # print out the date's individual components
 # print(today.day, today.year, today.month)
 # print(today.weekday)  
  # retrieve today's weekday (0=Monday, 6=Sunday)

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
 # days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
 # print(days[today.weekday()])


  # Get the current time
 today = datetime.time(datetime.now())
 print(today)

  
if __name__ == "__main__":
  main();
  