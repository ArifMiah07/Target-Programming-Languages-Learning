# 3.2. First Steps Towards Programming
# Of course, we can use Python for more complicated tasks than adding two and two together. For instance, we can write an initial sub-sequence of the Fibonacci series as follows:

# >>>
# Fibonacci series:
# the sum of two elements defines the next
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a+b

# 0
# 1
# 1
# 2
# 3
# 5
# 8


# fibonacci series
a, b = 0, 1

while a < 100 : 
    print(a)
    a, b = b, a + b
    

