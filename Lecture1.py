print('Hello, World!')

# Wrapping angles
print((265 + 180)%360)

# Rounding
c = round(1.1/3, 4)
print(c)

# Swapping variables
a = 3
b = 15.2
print('Before:',a,b)
a,b = b,a
print('After:',a,b)

# Strings
name = 'Monty Python'
title = 'Holy Grail'

full_title = name + ' and the ' + title
print(full_title)

# Every other character
print(name[::2])
print(name[1::2])
print(name[1:8:2])

print('Hello! ' * 10)

# Count how many 'ns' are in the variable name
print(name.count('n'))

# Replacing
print(name.replace('o','a'))

# Data types
x = '3.14'
y = float(x)
z = int(y)

print(x,y,z)

# Lists

apollo_moon = [11,12,14,15,16,17]

print(apollo_moon)

apollo_commanders = ['Armstrong','Conrad','Shepard','Scott','Young','Cernan']

print('Post-13 commanders:',apollo_commanders[2:])

apollo_commanders[0] = 'Lovell'

print('If Neil got sick:',apollo_commanders)

# Appending
apollo_moon.append(18)
apollo_moon.append(19)

print('Added cancelled missions:',apollo_moon)

# Removing last entry
cancelled = apollo_moon.pop()

print(cancelled)
print(apollo_moon)

# Insert failed Apollo 13
apollo_moon.insert(2,13)
print(apollo_moon)

# Remove entry by value
apollo_moon.remove(13)
print(apollo_moon)

# Remove by index
apollo_moon.pop(-1)
print(apollo_moon)

print('Index of Apollo 11:', apollo_moon.index(11))
print('Commander of Apollo 16:',apollo_commanders[apollo_moon.index(16)])

# Reverse list in place
apollo_moon.reverse()
print(apollo_moon)

# Reverse without modifying
print('Back to normal:',apollo_moon[::-1])

# List unpacking
apollo12_crew = ['Pete','Rick','Al']
commander, cm_pilot, lm_pilot = apollo12_crew
print(commander,cm_pilot,lm_pilot)

# 2D list
list2d = [[1,2],[3,4]]
print(list2d)
print(list2d[0][1])

mission_details = [1969, 'Apollo 12', ['Conrad', 'Gordan', 'Bean'], 10.19194]

# How to print 'Al Bean'
print(apollo12_crew[-1] + ' ' + mission_details[2][-1])

ww2 = [1939, 1940, 1941, 1942, 1943, 1944, 1945]

# Convert every element into string
ww2 = list(map(str,ww2))
print(ww2)

# Joining list members by a delimiter
print(', '.join(ww2))

# Other list operators
x = [1, 2, 20, 21, 22, 23, 1, 1]

print(sum(x))
print(max(x))
print(min(x))
print(x.count(1))

# Sorting list in place
x.sort()
print(x)

x.reverse()
print(x)

# Sorting list in descending order
print(list(reversed(sorted(x))))

# Lists: shallow vs deep copy

a = [1, 2, 3, 4]
b = a

print(a,b)

a[0] = 100

print(a,b)

# Make a copy of a
b = list(a)

a[0] = 0
print(a,b)
