# Sets in Python

# A set is a collection of unique and unordered values.

# 1. Creating a Set

numbers = {1, 2, 3, 4}
print("Set:", numbers)

# 2. Sets Do Not Allow Duplicate Values


numbers = {1, 2, 3, 4}
print("Set without duplicates:", numbers)


# 3. Creating an Empty Set


empty_set = set()
print("Empty set:", empty_set)


# 4. Adding an Item

numbers = {1, 2, 3}
numbers.add(4)
print("After adding 4:", numbers)


# 5. Adding Multiple Items

numbers = {1, 2, 3}
numbers.update({4, 5, 6})
print("After adding multiple items:", numbers)


# 6. Removing an Item

numbers = {1, 2, 3, 4}
numbers.remove(3)
print("After removing 3:", numbers)


# 7. Discarding an Item

numbers = {1, 2, 3, 4}
numbers.discard(3)
print("After discarding 3:", numbers)


# 8. Difference Between remove() and discard()

# remove() gives an error if the item does not exist.
# discard() does not give an error if the item does not exist.

numbers = {1, 2, 3}
numbers.discard(10)
print("After discard:", numbers)


# 9. Clearing a Set

numbers = {1, 2, 3}
numbers.clear()
print("After clear:", numbers)


# 10. Length of a Set

numbers = {10, 20, 30, 40}
print("Number of items:", len(numbers))


# 11. Checking if an Item Exists


numbers = {1, 2, 3, 4}
print("Is 3 in the set?", 3 in numbers)
print("Is 10 in the set?", 10 in numbers)


# 12. Checking if an Item Does Not Exist


numbers = {1, 2, 3, 4}
print("Is 10 not in the set?", 10 not in numbers)


# 13. Looping Through a Set


fruits = {"apple", "banana", "orange"}
print("Fruits:")

for fruit in fruits:
    print(fruit)


# 14. Union

# Union combines the items from two sets.
# Duplicate items are included only once.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print("Union:", result)


# 15. Intersection


# Intersection gives the items that exist in both sets.

set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1.intersection(set2)
print("Intersection:", result)


# 16. Difference


# Difference gives the items that are in the first set

# but not in the second set.

set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1.difference(set2)
print("Difference:", result)


# 17. Symmetric Difference


# Gives the items that are in either set,

# but not in both.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.symmetric_difference(set2)
print("Symmetric difference:", result)


# 18. Subset


# A set is a subset if all of its items

# are present in another set.

small_set = {1, 2, 3, 4}
large_set = {1, 2, 3, 4, 5, 6, 7}
print("Is small_set a subset?", small_set.issubset(large_set))


# 19. Superset


# A set is a superset if it contains all

# the items of another set.

small_set = {1, 2}
large_set = {1, 2, 3, 4}
print("Is large_set a superset?", large_set.issuperset(small_set))


# 20. Disjoint Sets


# Two sets are disjoint when they have no items in common.

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("Are the sets disjoint?", set1.isdisjoint(set2))


# 21. Copying a Set


numbers = {1, 2, 3}

new_numbers = numbers.copy()

print("Original set:", numbers)
print("Copied set:", new_numbers)


# 22. Converting a List to a Set


# This is useful when we want to remove duplicate values.

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)
print("Original list:", numbers)
print("Set:", unique_numbers)


# 23. Converting a Set to a List


numbers = {1, 2, 3, 4}

number_list = list(numbers)
print("Set:", numbers)
print("List:", number_list)


# 24. Updating a Set with Union

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print("Updated set:", set1)


# 25. Updating a Set with Intersection


set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print("After intersection update:", set1)


# 26. Updating a Set with Difference


set1 = {1, 2, 3, 4}
set2 = {2, 3}

set1.difference_update(set2)

print("After difference update:", set1)


# 27. Updating a Set with Symmetric Difference


set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.symmetric_difference_update(set2)

print("After symmetric difference update:", set1)
