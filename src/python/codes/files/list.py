square_value = [1, 4, 9, 16, 25, 36]

print(square_value) 

# ike strings (and all other built-in sequence types), lists can be indexed and sliced:

# >>>
# squares[0]  # indexing returns the item
# 1
# squares[-1]
# 25
# squares[-3:]  # slicing returns a new list
# [9, 16, 25]

print(square_value[0])
print(square_value[-1])
print(square_value[-2:])
print(square_value[:3])
print(square_value[3:])

# Lists also support operations like concatenation:

# >>>
# squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubic_value = [1, 8, 27, 64, 125]
print(square_value + cubic_value)

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

# >>>
# cubes = [1, 8, 27, 65, 125]  # something's wrong here
# 4 ** 3  # the cube of 4 is 64, not 65!
# 64
# cubes[3] = 64  # replace the wrong value
# cubes
# [1, 8, 27, 64, 125]

cubes = [1, 9, 27, 64, 125]# 2*2*2 = 8 !=9 || 2**3 = 8 != 9
print(cubes)#[1, 9, 27, 64, 125]

#fix
cubes[1] = 8 #[1, 8, 27, 64, 125]
print(cubes)

# You can also add new items at the end of the list, by using the list.append() method (we will see more about methods later):

# >>>
# cubes.append(216)  # add the cube of 6
# cubes.append(7 ** 3)  # and the cube of 7
# cubes
# [1, 8, 27, 64, 125, 216, 343]

cubes.append(6**3)
# cubes
print(cubes)

# Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. Any changes you make to the list through one variable will be seen through all other variables that refer to it.:

# >>>
# rgb = ["Red", "Green", "Blue"]
# rgba = rgb
# id(rgb) == id(rgba)  # they reference the same object
# True
# rgba.append("Alph")
# rgb
# ["Red", "Green", "Blue", "Alph"]

developer = ["PHP", "JAVASCRIPT", "PYTHON", ".NET"]
new_developer = developer
print(new_developer == developer)
print(new_developer, developer)
new_developer.append("RUST")
print(new_developer, developer)

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:

# >>>
# correct_rgba = rgba[:]
# correct_rgba[-1] = "Alpha"
# correct_rgba
# ["Red", "Green", "Blue", "Alpha"]
# rgba
# ["Red", "Green", "Blue", "Alph"]

right_new_developer = new_developer[:]
right_new_developer[0] = "Ruby"

print(new_developer)
print(right_new_developer)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

# >>>
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # replace some values
# letters[2:5] = ['C', 'D', 'E']
# letters
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# # now remove them
# letters[2:5] = []
# letters
# ['a', 'b', 'f', 'g']
# # clear the list by replacing all the elements with an empty list
# letters[:] = []
# letters
# []

char = ['1', '2', '3', '4', '5', 'd', 'r', 'e', 'f']
print(char)
char[2:5] = ['two', 'three', 'four']
print(char)
char[2:5] = []
print(char)
char[:] = []
print(char)

# The built-in function len() also applies to lists:

# >>>
# letters = ['a', 'b', 'c', 'd']
# len(letters)
# 4
numbers_list = [1, 4,5,6,7,8,9,9,0,0]
print(len(numbers_list))#10
print(numbers_list[1])


# It is possible to nest lists (create lists containing other lists), for example:

# >>>
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# x
# [['a', 'b', 'c'], [1, 2, 3]]
# x[0]
# ['a', 'b', 'c']
# x[0][1]
# 'b'

mix_char = ['a', 'b', 'c', 'd', 'e']
mix_number = [1,2,3,4,5,6,7]
mix_var = [mix_char, mix_number]

print(mix_char)
print(mix_number)
print(mix_var)

print(mix_var[0])
print(mix_var[0][0])