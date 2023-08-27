![Image of Waldo from "Where's Waldo"](../images/sets_intro.jpg)

# Sets
For the record, sets really would be the data structure that crushes the competition in "Where's Waldo". But, Sets are more properly characterized in technology as the data structure that's great at determining membership.
 
Interestingly, sets are able to exceed at being able to determine whether it is storing a particular data value, even though it never attempts to sort its incoming data.  

**Sets are highly efficient at sorting due to hashing.**

&nbsp;
## Hashing
Hashing is a powerful process that has a lot of different applications in technology today, including the fields of cybersecurity and database management. While its actual implementation details may differ based on the application, hashing always provides a means by which information can be broken down into smaller bits of information that's completely unique and easily retrievable.

Hashing occurs when elements are either stored in or retrieved from a **hash table.**

### Hash Tables
A hash table is a kind of data structure that stores each element from a set as a unique key-value pair. The element's index in the table is computed using the hashing process. 

During this process, the element's key is inputted into a **hash function** that computes **hash code**. The hash code is always an integer, even if the key is not, so it can be used to compute the element's index value within the table. 

Hashing makes it possible to instantaneouly locate an element's index, so elements can be added, removed, and retrieved in O(1) time. 

![Chart displaying the steps of the hashing process](../images/hashing_process.jpg)

**Non-hashable elements include:**

&nbsp;
## Set Implementation
A populated set can be created using **curly braces:**

```python
    colors = {'red', 'green', 'blue'}
```

Or, a set can be created using Python's **built-in set() function:** 

```python
    sports = set('soccer', 'volleyball', 'football')
```

The set() function **must be used when creating an empty set**. A
set of empty curly brackets will create a dict instead:
```python
    emptyDict = {}
    emptySet = set()

    print(type(emptyDict)) # <class 'dict'>
    print(type(emptySet))  # <class 'set'>
```

Keep in mind that these two methods are **not one in the same:**
* Curly braces accept objects as arguments, so the input is left as is.
    ```python
    new_set = {<obj>, <obj>, ..., <obj>}
    ```
* set() accepts iterables as arguments, so it will break up the input, 
thereby creating a list of elements to put in the set.
    ```python
    new_set = set(<iter>)
    ```

Thus, identical arguments will produce different results based
on the implementation method used:
```python
    obj_argument = {'abc'}    
    iter_argument = set('abc') 

    print(obj_argument)   # {'abc'}
    print(iter_argument)  # {'a', 'b', 'c'}
```

&nbsp;
## Characteristics 
* Elements are not stored in any particular order.
* All elements must be unique.
* Sets can be changed, but only immutable data types may be stored in a set.


### Removing Duplicates
All elements in a set must be unique because the hash code created
by two duplicate keys will also be the same. Thus, only the first
element to be hashed will be placed in the hash table. The second element
will not be added when it's intended index location is already occupied
with an element that shares the same hash code.

```python
    set_duplicateObjects = {'NV', 'AK', 'CO', 'TN', 'NV', 'NY'}      
    set_duplicateIterables = set('zzyzx') 

    print(set_duplicateObjects)   # {'TN', 'AK', 'NY', 'CO', 'NV'}
    print(set_duplicateIterables) # {'y', 'x', 'z'}
```
Note that both sets are not alphabetically ordered because
the value of each element does not affect its placement. The
hash code corresponding to each element will determine its
placement. In addition, the order of elements usually changes
each time the program is run. Certain factors like an element's 
location in memory (which also varies each time the program is
run) will influence the hash code.

## Operations 

  operation   |     description     |  performance
------------- | ------------------- | -------------
add(value)    | "value" is added to |  O(1)
              | the set             |
              |                     |
remove(value) | "value" is removed  |  O(1)
              | from the set        |
              |                     |
member(value) | indicates whether   |  O(1)
              | "value" is or isn't |
              | in the set          |
              |                     |
size          | returns  the total  |  O(1)
              | number of elements  |
              | in the set          |
              |                     |

```python
# Creating a set
fruits = {'apple', 'banana', 'orange', 'grape', 'kiwi'}

# Display the initial set
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
```
### add(value)


### remove(value)


### member(value)


### size()

in is a Python operation that can check if an element is part of an iterable
