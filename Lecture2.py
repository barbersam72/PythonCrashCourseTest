# While loop (Fibonacci sequence)

a, b = 0, 1
while b < 50:
    print(b, end=',')
    a, b = b, a + b

# Ctrl-/ comments anything highlighted

# Booleans
print()
print(1 == 1)
print(1 == 2)
print(True == 1)
print(False == 0)

# None
var = None
if var is None:
    print('The variable is None')

# Logical operators:
# and, or, ^ (xor), not

# Testing strings
test_str = "It's dangerous to go alone. Take this!"

if 'dangerous' in test_str:
    print('Thanks!')

# Testing lists
test_list = [1,2,3,4,5]

if 5 in test_list:
    print(test_list)

# Lists as conditions
test_list = []
if test_list:
    print('List not empty')
else:
    print('List empty')

# Find a number that is divisible by 2, 3, and 7 at the same time
x = 1
while x < 100:
    if (x % 2 == 0) and (x % 3 == 0) and (x % 7 == 0):
        print(x)
        break
    x += 1

# Leap years from 1990 to 2030
year = 1990
while year < 2030:

    year += 1

    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        print(year, 'leap')
        continue

    print(year)

# List enumeration + zip
cities = ['New York', 'London', 'Paris']
for i in enumerate(cities):
    print(i)

countries = ['USA', 'UK', 'France']
for j in zip(cities, countries):
    print(j)

# Reading file
file_name = 'data.txt'

with open(file_name, 'r') as f:

    print(f.closed)
    print(f.readline())

print(f.closed)

# Reading file line by line
with open(file_name) as f:
    for line in f:
        print(line)

a = 'one,two,three,four'
print(a.split(','))

b = '           center            '
print(b.strip())

# Printing file contents as list
with open(file_name) as f:

    for line in f:

        # Remove newline character

        line = line.replace('\n','')

        # Split line into list

        line = line.split(',')

        print(line)