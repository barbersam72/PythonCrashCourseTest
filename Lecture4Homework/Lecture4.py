# Functions
def decimalHour(time_string):
    'Converts time from 24h hh:mm:ss to decimal hours'

    hh, mm, ss = time_string.split(':')
    hh, mm, ss = map(float, (hh, mm, ss))

    result = hh + mm/60 + ss/3600

    return(result)

print(decimalHour('05:29:45'))

def UTCdecimal(time_string, timezone = 0):
    '''Converts time from 24h hh:mm:ss to decimal hours,
    with respect to time zone'''

    result = decimalHour(time_string) + timezone

    return result%24

print(UTCdecimal('05:29:45',timezone=-7))

# Local vs global variables

SPEED_OF_LIGHT = 300_000

def test(var):
    print('Input:',var)

    var = 20

    print('Changed:',var)

    print('c =',SPEED_OF_LIGHT)

var = 10

test(var)

print('Global:',var)

# Unpacking function arguments

def isTriangle(a,b,c):
    '''Check if given triangle sides can form a triangle'''

    if c > (a + b):
        return False
    elif b > (a + c):
        return False
    elif a > (b + c):
        return False
    
    return True

triangle_sides = [2,3,4]

print(isTriangle(*triangle_sides))

# How to name things:
# variable_names
# functionNames
# ClassNames
# CONSTANT_NAMES

# Numpy
import numpy as np

a = [[5, 1, 8], [3, 4, 6]]

print(a)

# Convert to numpy array
a = np.array(a)
print(a)

print('Shape:',a.shape)
print('Dimensions:',a.ndim)
print('Type:',a.dtype)
print('Total # of elements:',a.size)

b = np.zeros((3,3))
print(b)
print(b.dtype)

c = np.ones((3,3), dtype=int)
print(c)

# Identity matrix
idm = np.eye(3)
print(idm)

# Converting string list to floats
num_lst = ['1.20','2.15','3.78','4.05']

num_lst = np.array(num_lst).astype(np.float64)
print(num_lst)

# Create range of numbers from 0 to 100 in steps of 0.5
arr = np.arange(0, 100, 0.5)
print(arr)

# Create range of numbers with fixed # of elements
arr2 = np.linspace(0, 2, 9)
print(arr2)

# Reshaping an array
arr2 = arr2.reshape((3,3))
print(arr2)

# Adding a scalar to an array
a = np.zeros((3,3))
a = a + 5
print(a)

# Multiplying
a = a * 3
print(a)

a = np.zeros((3,3)) + 2
b = np.zeros_like(a) + 3

print(np.dot(a,b))

a = np.arange(1,101)
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))

# Arrays for plotting

arr = np.linspace(1,5,20)

print(np.sqrt(arr))
print(np.sin(arr))
print(np.cos(arr))
print(np.exp(arr))

# Plotting

import matplotlib.pyplot as plt

# Sine function in range x = [0,10] radians
x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)

plt.title('My plot')
plt.xlabel('x')
plt.ylabel('sin x')

plt.grid()

plt.show()
