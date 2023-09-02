# Creates a set using string objects as arguments
fruits = {'apple', 'banana', 'orange', 'grape', 'kiwi'}

# Initial set: {'banana', 'grape', 'orange', 'apple', 'kiwi'}
print("Initial set:", fruits) 

# Adds an element to the set
fruits.add('pear')

# After adding 'pear': {'banana', 'grape', 'orange', 'apple', 'pear', 'kiwi'}
print("After adding 'pear':", fruits)

# Removes an element from the set
fruits.remove('banana')

# After removing 'banana': {'grape', 'orange', 'apple', 'pear', 'kiwi'}
print("After removing 'banana':", fruits)

# Check 'kiwi' & 'banana' for membership
print("'kiwi' in fruits:", 'kiwi' in fruits)       # 'kiwi' in fruits: True
print("'banana' in fruits:", 'banana' in fruits)   # 'banana' in fruits: False