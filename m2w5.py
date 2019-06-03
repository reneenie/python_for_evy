# dictionary
# key + value combo

# one useful way: word count
a = dict()
a['Amy']=1
a['Eason']=2
a['Bob']=1
print(a)

######### histgram results of dictionary
words = ['a','v','a','c','c','a']
tmp = dict()
for key in words:
    if not key in tmp:
        tmp[key] = 1
    else: tmp[key] = tmp[key]+1
print(tmp)

# get method in dictionary
tmp2 = dict()
for key in words:
    tmp2[key] = tmp2.get(key,0)+1
print(tmp2)
## 0 is the default value for keys not in the dictionary


######### tuples data structure
# output a list of keys
print('output of list:',list(tmp))
print('output of keys method:',tmp.keys())
# output a list of values
print('output of values method:',tmp.values())


# use item method to get tuples
print('output of item method:',tmp.items())

######### bonus: two iteration variables in python
for key, value in tmp:



######### Chap 9 quiz
stuff = dict()
print(stuff.get('candy',-1))


######### Chapt 9 assignment
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
