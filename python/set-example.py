"""input = ['not', 'hashable']
hash(input)"""
# Creates a set using string objects as arguments
fruits = {'apple', 'banana', 'orange', 'grape', 'kiwi'}


print("Initial set:", fruits)

# Adding an element to the set
fruits.add('pear')
print("After adding 'pear':", fruits)

# Removing an element from the set
fruits.remove('banana')
print("After removing 'banana':", fruits)

# Checking membership
print("'kiwi' in fruits:", 'kiwi' in fruits)
print("'banana' in fruits:", 'banana' in fruits)

# Creating another set for set operations
citrus_fruits = {'orange', 'lemon', 'lime'}

# Union of sets
all_fruits = fruits.union(citrus_fruits)
print("Union of sets:", all_fruits)

# Intersection of sets
common_fruits = fruits.intersection(citrus_fruits)
print("Intersection of sets:", common_fruits)

# Difference of sets
non_citrus_fruits = fruits.difference(citrus_fruits)
print("Difference of sets:", non_citrus_fruits)