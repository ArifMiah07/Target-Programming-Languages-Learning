a = 'hello world'
b = 'Don\'t I?'
c = 'Oh my lord plz help us.\n Help us'
d = r'Fi\ne'

print(a, b, c, d, "")

#String literals can span multiple lines
print(""" 
      Joseph: Hi Mark!!
      Leo: Hey there. What upp???
      Joseph: Hey see this JSON data.
      Leo: Ok. Show me.
      Joseph: Look...{
      "model": "MX TO XLK",
      "date": "2025-12-3",
      "data" : [
          'A', 
          'B',
          {
              "cName": "Mark Twit"
          }
      ]
      }
""")

#Strings can be concatenated (glued together) with the + operator, and repeated with *:

concat_str = 1 * "Y" + 10 * 'a' + "h" + " " + "Allah" + " " + "Help Us" #Yaaaaaaaaaah Allah Help Us
d_str = "\nHi" " " "Mom" "!" #Hi Mom!
d_str_2 = "\nGood Morning!"
print(concat_str, d_str)
print(d_str + d_str_2)

print(d_str_2[1], d_str_2[6], d_str_2[-5], d_str_2[-1])
# slicing
# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

# >>>
# word[:2]   # character from the beginning to position 2 (excluded)
# 'Py'
# word[4:]   # characters from position 4 (included) to the end
# 'on'
# word[-2:]  # characters from the second-last (included) to the end
# 'on'
word = 'PyThon'
print(word[0: 2])
print(word[2: 5])
print(word[-1])
print(word[:2])
print(word[2])
print(word[-2:])

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

# >>>
# word[:2] + word[2:]
# 'Python'
# word[:4] + word[4:]
# 'Python'

print(word[2:] + word[:2])
print(word[:2] + word[2:])
print(word[:4] + word[4:])
print(word[3:] + word[:3])

# if you need a different string, you should create a new one:

# >>>
# 'J' + word[1:]
# 'Jython'
# word[:2] + 'py'
# 'Pypy'

print(word[:2] + 'Yep' + word[2:]) 

# The built-in function len() returns the length of a string:

# >>>
# s = 'supercalifragilisticexpialidocious'
# len(s)
# 34

print(len(word)) #6