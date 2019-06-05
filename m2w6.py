# Tuple data structure
# 1. immutable: cannot be modified


# things not to do with tuple
######### will return traceback!!!
# tuple.sort()
# tuple.append()
# tuple.reverse()

# assign values to tuple
(x,y) = ('Amy', 4)
print((x,y))

# compare tuple
# compare the first one first.
# if the first ones are equal, goes to the second one and so on

print((0,1,2) < (5,0,1))
print((0,0,1) < (0,2,1))
print(('B','a','A') < ('a','a','A')) # uppercase always < lowercase, and posterior letters > prior letters


### key difference between tuples and lists
# it doesn't have to build these structures to be changeable,
# and so they're just more efficient and more performant than lists.
# for Lists, you have to actually allocate extra memory and stuff like that to let them be changed

# quiz
# x , y = 3, 4
# print('y:',y)


# sorting dictionary using key order
# ! keys in dictionary have to be unique
# ! dictionary doesn't record order

a = dict()
a['Amy']=1
a['Eason']=2
a['Bob']=1
print(a)

# 1. sort tuples by key orders
a_sortbyKey = sorted(a.items())
for k, v in a_sortbyKey:
    print('sort tuples by key orders',k,v)

# 2. sort tuples by value orders
tmp = []
for k,v in sorted(a.items()):
    tmp.append((v,k))
a_sortbyValue = sorted(tmp,reverse=True)
for v,k in a_sortbyValue:
    print('sort tuples by value orders',k,v)

########## List comprehension
# format: [ expression for item in list if conditional ]
# equivalent to
# for item in list:
#     if conditional:
#         expression

print(sorted([(v,k) for k,v in a.items()],reverse = True))


########## Assignment ###############
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour_dict = dict()
for line in handle:
    parts = line.split()
    if line.startswith('From') == False or len(parts) < 6:
        continue
    timestamp = parts[5]
    print(timestamp)
    time = timestamp.split(':')
    hour_dict[time[0]] = hour_dict.get(time[0],0)+1

for k,v in sorted(hour_dict.items()):
    print(k,v)
