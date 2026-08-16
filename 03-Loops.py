# Loops in Python

# ----------------

# Loops are used to repeat a block of code.

# 1. for loop

# Basic syntax:

# for variable in sequence:

# code

print("For loop:")

for i in range(5):
 print(i)

# 2. while loop

# Basic syntax:

# while condition:

# code

print("\nWhile loop:")

count = 1

while count <= 5:
 print(count)
 count += 1

# 3. range()

# range(start, stop, step)

print("\nUsing range():")

for i in range(2, 11, 2):
 print(i)

# 4. Looping through a list

print("\nLooping through a list:")

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
 print(fruit)

# 5. break

# Stops the loop completely.

print("\nUsing break:")

for i in range(1, 10):
 if i == 5:
  break
print(i)

# 6. continue

# Skips the current iteration.

print("\nUsing continue:")

for i in range(1, 6):
 if i == 3:
  continue
print(i)

# 7. Nested loops

# A loop inside another loop.

print("\nNested loops:")

for i in range(1, 3):
  for j in range(1, 4):
   print("i =", i, "j =", j)
