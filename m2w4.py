# list mutable
# two ways to loop through a list

letters = ['a', 'd', 'r']

# 1. iteration loop
for letter in letters:
    print('The list has letter',letter)

# 2. counted loop
for i in range(len(letters)):
    letter = letters[i]
    print('The',i+'th','letter is', letter)
