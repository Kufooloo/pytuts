#
# Example file for working with loops
#
import datetime
def main():
  x = 0

  # define a while loop
  # while (x<5):
   # print(x)
   # x = 1 + x

  # define a for loop
  # for x in range(5, 10):
   # print(x)

  # use a for loop over a collection
  # days = ["Mon","Tues","Weds","Thur","Fri","Sat","Sun"]
  # for d in days:
   # print(d)
	
  # use the break and continue statements
  # for x in range(5,10):
   # # if (x==7) : break
   # if (x%2 ==0): continue
   # print(x) 

  #using the enumerate() function to get index 
  days = ["Mon","Tues","Weds","Thur","Fri","Sat","Sun"]
  for i in enumerate(days):
   print(i)
   
if __name__ == "__main__":
  main()
