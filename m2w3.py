# file handle
# x = open('file.txt','r')

# the newline character
tmp = 'Hello\nworld'
print(tmp)
print(len(tmp)) # newline character has length 1

# assignment approach 1
# filename = input('Enter the file name: ')
# tmp = open(filename)
# count = 0
# for line in tmp:
#     l = line.rstrip()
#     print(l.upper())
#     count += 1
# print('There are',count,'lines.')

# assignment approach 2
# txt = tmp.read()
# print(txt.upper().rstrip())

# assignment 2
# file = input('Enter the 2nd file name: ')
# tmp2 = open(file)
# total = 0.0
# count = 0
# for line in tmp2:
#     if line.startswith('X-DSPAM-Confidence:')==True:
#         start = line.find(':')
#         count += 1
#         total += float(line[start+1:].strip())
# print('Average spam confidence:',total/count)

# assignment2 better way
file = input('Enter the 2nd file name: ')
tmp2 = open(file)
total = 0.0
count = 0
for line in tmp2:
    if not line.startswith('X-DSPAM-Confidence:')==True:
        continue
    start = line.find(':')
    count += 1
    total += float(line[start+1:].strip())
print('Average spam confidence:',total/count)
