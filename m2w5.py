# list mutable
# two ways to loop through a list

letters = ['a', 'd', 'r']

# 1. iteration loop
for letter in letters:
    print('The list has letter',letter)

# 2. counted loop
for i in range(len(letters)):
    letter = letters[i]
    # if you want to use + to connect output strings w/o space, like in java,
    # need to convert it to string first
    print('The '+str(i)+'th','letter is', letter)

# concatenating lists
list_a = [2,4,6]
list_b = [1,5,7]
print(list_a+list_b)

# slicing lists
# up to but not including


# building lists from scratch
a = []
a.append(9)
a.append(2)
a.append(6)
print(a)
print(a.append(3)) # cannot print any function within the class that mutate the object

# sort lists
a.sort()
print(a)

# calculation within lists
print(sum(a))
print(len(a))
print(max(a))
print(min(a))

# list and strings
# stuff = letters.split()
# print(stuff)
# for letter in stuff:
#     print(letter)

# specify delimiter in split()

# assignment 1 by lei
file = open('romeo.txt')
words = []
for line in file:
    tmp = line.strip().split()
    for word in tmp:
        if word in words:
            continue
        words.append(word)
words.sort()
print(words)

# assignment2 by lei
file2 = open('mbox-short.txt')
count = 0
for line in file2:
    line.strip()
    if not line.startswith('From '):
        continue
    line_list = line.split()
    count += 1
    print(line_list[1])
print('There were',count,'lines in the file with From as the first word')

# assignment 2 better:
file2 = open('mbox-short.txt')
count2 = 0
for l in file2:
    wd = l.rstrip().split()
    if len(wd) < 2 or wd[0] != 'From':
        continue
    count2 += 1
    print(wd[1])
print('There were',count2,'lines in the file with From as the first word')
