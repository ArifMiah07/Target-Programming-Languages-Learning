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
# import random

# print(random.randrange(1, 10))

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

import random
for i in range(3):
  print(random.randrange(1, 6))
  
# string are array
x = 'ni hao'
print(x[1])  
# Looping Through a String
x1 = 'baannnaananaa'
for x in x1:
  print(x)

# String Length
x2 = 'hello world'
print(len(x2))

# Check String
txt = 'The best things in life are free!'
print('free' in txt)  

if 'free' in txt:
  print('yes that true ' )
else:
  print('a false statement is always false but if this true than how its a false statement?')
print('expensive' in txt)
if 'expensive' not in txt:
  print('no no that is not true')
  
  # Slicing
b1 = 'is earth is not better than hell?'
print(b1[0:len(b1)])
print(b1[:len(b1)])
print(b1[0:])

# Negative Indexing
print(b1[-len(b1): -2])
print(b1[-9: -5])

# Upper Case

bd = 'bangladesh'
print(bd.upper())
# bd = 'bangladesh'
# Lower Case
print(bd.upper().lower())

# Remove Whitespace
k1 = '   hello world   '
print(k1.strip())

# Replace String
k9  = 'hilter is a good goy'
h10 = (k9.replace('lt', '**'))
print(h10.replace('oy', 'uy'))

# Split String
b3 = 'heil nein'
print(b3.split(" "))
# String Concatenation
e2 = 'heil'
e3 = 'nein'
print(e2+" "+e3)

# String Format
name = 'hilter'
txt = f"heil {name}! {name} is a good goy!"
print(txt)

# Placeholders and Modifiers
prince = float(40.6)
print(f"{prince:.2f}") 
price = int(39)
print(f"total price: {price * 7} usd")
# Escape Character
print(f"\xf8")
print("We are the so-called \"Vikings\" from the north.")
# 
txt = "0"

x = txt.zfill(10)
for i in range(len(x)):
	print(f"{txt} {'\t' * i}", end="")
for j in range(len(x)):
	print(f"{txt} {'\n' * i}", end="") 
 
#  
# String Methods
# Python has a set of built-in methods that you can use on strings.

# Note: All string methods return new values. They do not change the original string.

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

#@||| Python Booleans |||
# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

# Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

# Example
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))

# Python Operators

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator	Name	Example	Try it
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

# 
user_perm = 0b0110
user_perm &= 0b0010
print(bin(user_perm))  # Output: 0b10



# 
EDIT = 0b0010
DELETE = 0b0100

user_perm = EDIT
user_perm |= DELETE  # Give user delete permission
print(bin(user_perm))  # Output: 0b110

x = 0b0110  # Edit + Delete
x ^= 0b0010  # Toggle Edit
# Result: 0b0100 → Now only Delete
# ✔️ This is like:

# “If permission exists, remove it.
# If it doesn’t exist, add it.”

# Use case: Toggle a feature/flag without checking first.

x = 0b1000  # 8
x >>= 2
# Result: 0b0010 → 2
# ✔️ Each right shift >> 1 = divide by 2

x = 0b0011  # 3
x <<= 2
# Result: 0b1100 → 12
# ✔️ Each left shift << 1 = multiply by 2

# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name	Example	Try it
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y

# 
# Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y	

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y


# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator	Name	Description	Example	Try it
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# Operator Precedence
# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	Description	Try it
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR
# If two operators have the same precedence, the expression is evaluated from left to right
