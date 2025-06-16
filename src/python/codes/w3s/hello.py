# say hello world
print("hello, world!")

###
# indentation
if 5 > 2:
  print("Five is greater than two!")

###
# variables 
# camel case => myVariableName
# Pascal case => MyVariableName 
# Snake case => my_variable_name
## Assign Multiple Values
x,y,z = "a", 'bcd', 'alphabet'
print(x,y,z)
# one value to multiple variables
x=y=z = "color"
print(x,y,z)
# Unpack a Collection
colors = ['red', 'green', 'yellow']
x, y, z = colors
print(x,y,z)
# Global Variables
x = 'awesome'
def myFunc() : 
  global x
  x = 'fantastic'
  print('python is ' + x)

myFunc()
print('python is ' + x)

# Built-in Data Types
## String  # str => string
## Number
  # int => integer
  # float => floating
  # complex => maybe imaginary numbers or vector
## Sequence Types:
  # list
  # tuple
  # range
## Mapping Type : 
  # dict
## Set types
  # set
  # frozenset
# Boolean Types : 
  # bool
# Binary Types : 
  # bytes 
  # bytearray
  # memoryview
# None Type :
  # NoneType
  
##|||##
# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType
#@| get the data type by using the type() function |

# Setting the Specific Data Type
# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview

############# python is very weird! ############

# @| Float can also be scientific numbers with an "e" to indicate the power of 10.
##==> x = 35e3, y = 12E4, z = -87.7e100

# @|| Complex numbers are written with a "j" as the imaginary part:
# x = 3+5j
# y = 5j
# z = -5j

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# Note: You cannot convert complex numbers into another number type.

# Random Number
import random

print(random.randrange(1, 10))

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes: