import math

# dynamically typed language
n = 0
print(f'n is {n}')

# Multiple assignments
n, m, z = "hey", "Krishna", 100

# increment
n = 0
n += 1

# none is null
n = None

# if statements do not need paranthesis and does not need curly braces, uses indentation
if n is None:
    print(n)

# parenthesis needed for multi-line conditions
n, m = 1, 2  # unpacking
if (n > 2) and (n != m) or (n + 1) == m:
    print("Wow hold on")
    print(True)

# While loops
n = 10
while n <= 20:
    print(n)
    n += 2

# For Loops - print 0 - 5 and 5 - 1
print("---------------------------------------")
for i in range(6):
    print(i)
print("---------------------------------------")
for i in range(5, 0, -1):  # initial value, ending value and the number by which you want to increment or decrement
    print(i)

# Math - Division
print("---------------------------------------")
print(5 / 2)  # decimal division by default -> 2.5
print(5 // 2)  # double slash division rounds down -> 2
print(-3 / 2)  # gives -1.5 -> but we need -1 like other languages, // division gives -2 as it rounds down(lower)
print((int)(-3 / 2))  # workaround

# Math - Modulo Operator
print("---------------------------------------")
print(10 % 3)  # works well but not for negative values
print(int(math.fmod(-10, 3)))

# Math - Helper functions
print("---------------------------------------")
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(16))
print(math.pow(2, 4))

# Max and minimum values in Python
float("inf")
float("-inf")

# Python numbers are infinite and they never overflow
print(math.pow(2, 200) < float("inf"))

# Arrays
print("---------------------------------------")
arr = [1, 2, 3]
print(arr)

# STACKS -> Python arrays are dynamic and can be used as a stack as well
arr.append(4)
arr.append(5)
print(arr)
arr.pop()
print(arr)

arr.insert(0, 500)  # you can insert anywhere in an array -> index, value. It's a O(N)
print(arr)
arr[0] = 400  # inserting or reading from an array is O(1)
print(arr)

# initialise array size
print("---------------------------------------ARRAY")
n = 5
arr = [0] * n  # -> [0, 0, 0, 0, 0]
print(arr)
print(len(arr))
# CAREFUL! negative value in array index is actually the last element onwards
print(arr[-1], arr[-2])  # last 2 values

# sublists or slicing an array
print("---------------------------------------")
arr = [1, 2, 3, 4, 5]
print(arr[2:4])  # start from index 2 till index4(but 4 is not included) so 2 and 3 gets printed

# unpacking in arrays
a, b, c = [1, "haha", 4]  # unpacking requires us to have same variables on the left as that in the array
print(a, b, c)

# Looping through arrays - Important
print("---------------------------------------")
nums = [100, 200, 300]

# looping using index
for i in range(len(nums)):
    print(nums[i])

# for each loop, looping through just the values NO INDEX
for n in nums:
    print(n)

# unpacking the index and the value while looping(this is insane)
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously through unpacking using zip function
print("---------------------------------------")
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# reverse and sorting an array
print("---------------------------------------")
nums = [1, 2, 3]
nums.reverse()
print(nums)

nums.sort()
print(nums)

# sorting in reverse order
nums.sort(reverse=True)
print(nums)

# sorting strings
strings = ["Krishna", "Ankita", "Ashvin", "Rounak"]
strings.sort()
print(strings)

# custom sorting (by length of string)
strings.sort(key=lambda x: len(x), reverse=True)
# key -> lambda is a function without a name, value in the array is called x
# x is going to return the length of each string in the array. Then the array sorts by the length in the string. WOW
print(strings)

# List comprehension
print("---------------------------------------")
# advanced way of initialising lists using list comprehension
arr = [i for i in range(5)]  # output -> [0, 1, 2, 3, 4]
print(arr)

# 2-D Lists - this works, it creates one array with 4 (0) values and then
# the for loop takes that inner array and makes 4 of them for the outer array Matrix
matrix = [[0] * 4 for i in range(4)]
print(matrix)

# this 2-d array won't work -> all the values in rows are not unique, if you update one value, everything gets updated
matrix2 = [[0] * 4] * 4
print(matrix2)

# Strings are very similar to arrays
print("---------------------------------------")
s = "abc"
print(s[0:2])  # slicing a string

# Strings are immutable once created like Java, so you can't go and do
# s[0] = "A"

s += "def"  # new string gets created everytime you update it. Modifying a string is an N time operation
print("---------------------------------------")
# string to int and int back to string
print(int("123") + int("123"))
print(str(123) + str(123))

# looping through a string
str1 = "hello"
for s in str1:
    print(s)

# getting ascii value of a character
print("--------------------ASCII-------------------")
print(ord('a'))

# combine a list of strings using a delimiter
Strings = ["ab", "cd", "ef"]
print("".join(Strings))  # abcdef

# queues
from collections import deque

print("---------------------------------------")
queue = deque()
queue.append(1)  # append to the right
queue.append(2)  # adding values to the back of the queue
print(queue)

# pop from the left of the queue
queue.popleft()
# add to the front of the queue from the left
queue.appendleft(100)
print(queue)

# pop from the right side of the queue
queue.pop()
print(queue)

# Hash set -
"""

A Set is a generic set of values with no duplicate elements. 
A TreeSet is a set where the elements are sorted.
 A HashSet is a set where the elements are not sorted or ordered.
"""
print("------------------Hashset---------------------")
mySet = set()
mySet.add(1)  # in O(1) operation
mySet.add(2)
print(mySet)

print("len is ", len(mySet))  # len of set

print(1 in mySet)  # searching in constant time
print(200 in mySet)

mySet.remove(2)  # you can delete in constant time also
print(mySet)

# initialise set and list to set
print(set([1, 2, 3]))

# set comprehension
mySet = {i for i in range(5)}  # the for loop runs first and then adds that i to the left i
print(mySet)

# HashMap (aka dict)
print("------------------HashsMap---------------------")
myMap = {}
myMap["Krishna"] = 27
myMap["Ankita"] = 26
print(myMap)
print("len of map is ", len(myMap))
# the keys are unique. You can update the values
myMap["Ankita"] = 500
# printing the value
print(myMap["Ankita"])

# check if key in map
print("Krishna" in myMap)
# delete a key in map
print("--")
print(myMap.pop("Krishna"))
print(myMap)

# Manual insertion of values in HashMap
myMap = {"Tushar": 500, "DOnkey": 200}
print(myMap)

# dictionary comprehension
myDict = {i: 2 * i for i in range(3)}
print(myDict)

# looping through a dictionary through  either keys or values, both are possible
myMap = {"Tushar": 500, "DOnkey": 200}
for key in myMap:
    print(key, myMap[key])

for value in myMap.values():
    print(value)

# unpacking the key and value in a dict
for key, value in myMap.items():
    print(key, value)

# tuple - its like an array but immutable
print("------------------Tuple---------------------")
tup = (1, 2, 3)
print(tup)
print(tup[1])
# you can't do tup[0] = 55

# tuple can be used as key for HashMap or HashSet
myMap = {(1, 2): "Hello"}
print(myMap[(1, 2)])

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

# Functions
print("------------------function---------------------")


def myFunc(n, m):
    return n * m


def hello():
    print("sup bro")


print(myFunc(5, 10))
hello()


# nested function - It has access to outer variables
def outer(a, b):
    c = 'c'

    def inner():
        return a + b + c

    return inner()


print(outer('a', 'b'))


# using a nested function to double values in an array and a val
def double(arr, valBr):
    def helper():
        for x, y in enumerate(arr):
            arr[x] *= 2
            # now I can't do val * 2 because val scope will be only for the helper func
            # the workaround is to call the val as a nonlocal
            nonlocal valBr
            valBr *= 2
        helper()
        print(arr, valBr)


nums = [1, 2]
valBr = 3
double(nums, valBr)
