#
# Example file for working with functions
#

# define a basic function
def func1():
	print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
	print(arg1 ," ",  arg2)

# function that returns a value
def func3(x):
	return x*x*x

# function with default value for an argument
# def power(num, x=1):
	# result = 1;
	# for i in range(x):
		# result = result *num
	# return result
	

#function with variable number of arguments

def multi_arg(*args):
	result = 0;
	for x in args:
		result = result + x
	return result
# func2(20, 10)
# print(func2(20, 10))
# func1()
# print(func1())
# print(func1)
# func3(8)
# print(func3(8))
# print(power(5, 8))
# print(power(2))
print(multi_arg(10, 5, 5, 5))
