# Tuples are ordered and cannot be changed after they are created.

# Basic tuple
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Tuple with different types of values
student = ("Zayren", 18, 3.5)
print(student)

# A tuple can also be created without brackets
colors = "red", "green", "blue"
print(colors)


# Accessing tuple items
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[2])
print(numbers[-1])


# Slicing a tuple
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# Tuples cannot be changed
numbers = (10, 20, 30, 40)

# numbers[0] = 100
# This will give an error because tuples are immutable.


# Looping through a tuple
fruits = ("apple", "banana", "mango", "orange")

for fruit in fruits:
    print(fruit)


# Checking if an item exists
fruits = ("apple", "banana", "mango")

print("banana" in fruits)
print("grapes" in fruits)


# Tuple length
numbers = (10, 20, 30, 40, 50)
print(len(numbers))


# Joining tuples
first = (1, 2, 3)
second = (4, 5, 6)

result = first + second

print(result)


# Repeating a tuple

numbers = (1, 2)
print(numbers * 3)


# Counting an item
numbers = (1, 2, 2, 3, 2, 4)
print(numbers.count(2))


# Finding the position of an item
numbers = (10, 20, 30, 40)
print(numbers.index(30))


# Tuple unpacking
student = ("Zayren", 18, "Computer Science")
name, age, field = student

print(name)
print(age)
print(field)


# Nested tuple

students = (
    ("Ali", 18),
    ("Ahmed", 19),
    ("Sara", 18)
)

print(students[0])
print(students[1][0])


# Converting a list into a tuple

numbers_list = [1, 2, 3, 4]
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)


# Converting a tuple into a list

numbers = (1, 2, 3, 4)
numbers_list = list(numbers)
print(numbers_list)