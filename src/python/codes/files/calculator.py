# 3.1. Using Python as a Calculator
# Let’s try some simple Python commands. Start the interpreter and wait for the primary prompt, 
# >>>. (It shouldn’t take long.)

# 3.1.1. Numbers
# The interpreter acts as a simple calculator: you can type an expression at it and it will 
# write the value. Expression syntax is straightforward: the operators +, -, * and / can be used 
# to perform arithmetic; parentheses (()) can be used for grouping. For example:

a = 1
b = 2
c = 3
d = 4
e =5
f = 6

sum1 = a + b + c
sum2 = a - c - d
sum3 = a * b * c
sum4 = e / b
sum5 = a * (b - c) + d * (e - f)
sum6 = b * (c + a) - d * (e -f)
sum7 = a * (b*c) + d * (e / f)
sum8 = a * (b/c) - d * (e * f)

print(f"sum1: {sum1}")
print(f"sum2: {sum2}")
print(f"sum3: {sum3}")
print(f"sum4: {sum4}")
print(f"sum5: {sum5}")
print(f"sum6: {sum6}")
print(f"sum1: {sum1}")
print(f"sum8: {sum8}")

# a = int(input("a : "))
# b = int(input("b : "))
# c = int(input("c : "))

# num  = 3
# sum = a+b+c

# avg = sum / num 
# print(f"sum: {sum}")
# print(f"avg: {avg}")

# The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional 
# part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.

# Division (/) always returns a float. To do floor division and get an integer result you
# can use the // operator; to calculate the remainder you can use %:


numA = 12
numB = 5
numC = 2

result1 = numA / numB #Division (/) always returns a float
result2 = numA // numB #To do floor division and get an integer result you can use the // operator
result3 = numA % numB #to calculate the remainder you can use %

print(f"result1: {result1}")
print(f"result2: {result2}")
print(f"result3: {result3}")


# With Python, it is possible to use the ** operator to calculate powers [1]:

# pValA =  