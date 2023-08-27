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
An set can be created using **curly braces:**

```python
    new_set = {'a', 'e', 'i', 'o', 'u'}
```

Or, an empty set can be created using Python's **built-in set() function:** 

```python
    new_set = set()
```

Keep in mind that these two methods are **not one in the same:**
* Curly braces accept objects as arguments, so the input is left as is.
* set() accepts iterables as arguments, so it will break up the input, 
thereby creating a list of elements to put in the set.

```python
    set_object = {'abc'}    
    set_iterable = set('abc') 

    print(set_object)   # {'abc'}
    print(set_iterable) # {'a', 'b', 'c'}
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

### add(value)


### remove(value)


### member(value)


### size()

in is a Python operation that can check if an element is part of an iterable
