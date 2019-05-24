# changes from python2 to python3
# 1. print '' -> print('')
# 2. raw_input() -> input()
# 3. how to handle complex charaxters

# data structure 1: String
# input() always gives you strings

# SLICING begining and up to but not including
word = 'banana'
print(word[2:4])
print(word[:5])
print(word[2:])

# String comparison
'A' < 'a' # true
'z' > 'a' # return true
'Z' > 'A' # return true

# functions in string library
greet = 'Hi'
print(greet.lower())

# str.find()

# str.strip()
## str.lstrip()
## str.rstrip()

# str.replace()
