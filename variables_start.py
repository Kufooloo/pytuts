# 
# Example file for variables
#
f = 0
# Declare a variable and initialize it
print(f)

# # re-declaring the variable works
f = "abc"
print(f)

# # ERROR: variables of different types cannot be combined
print("string type" + str(123))

# Global vs. local variables in functions

def somefunction():
	f="def"
	print(f)
somefunction()
print(f)