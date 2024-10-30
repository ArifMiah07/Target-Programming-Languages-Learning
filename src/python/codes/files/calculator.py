a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

num  = 3
sum = a+b+c

avg = sum / num 
print(f"sum: {sum}")
print(f"avg: {avg}")



# advance

# def get_valid_input(prompt):
#     while True:
#         try:
#             # Attempt to convert input to an integer
#             value = int(input(prompt))
#             return value
#         except ValueError:
#             # Handle non-integer inputs
#             print("Invalid input. Please enter a valid integer.")

# # Get valid inputs from the user
# a = get_valid_input("a: ")
# b = get_valid_input("b: ")
# c = get_valid_input("c: ")

# # Ensure we have exactly three inputs
# num = 3
# sum_values = a + b + c
# avg = sum_values / num

# print(f"Sum: {sum_values}")
# print(f"Average: {avg}")
