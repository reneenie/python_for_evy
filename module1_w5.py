# 5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

while True:
    tmp = input("Enter an integer: ")
    if tmp == "done":
        break
    try:
        tmp = integer(tmp)
    except:
        print('Invalid input')
        continue
    if tmp > largest_so_far:
        largest_so_far = tmp
    if tmp < smallest_so_far:
        smallest_so_far = tmp
print('Maximum is',largest_so_far)
print('Minimum is',smallest_so_far)
