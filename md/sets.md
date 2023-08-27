![Image of Waldo from "Where's Waldo"](../images/sets_intro.jpg)

# Sets
For the record, sets really would be the data structure that crushes the competition in "Where's Waldo". But, Sets are more properly characterized in technology as the data structure that's great at determining membership.
 
Interestingly, sets are able to exceed at being able to determine whether it is storing a particular data value, even though it never attempts to sort its incoming data.  

**Sets are highly efficient at sorting due to hashing.**

&nbsp;
## Hashing
Hashing is a powerful process that has a lot of different applications in technology today, including the fields of cybersecurity and database management. While its actual implementation details may differ based on the application, hashing always provides a means by which information can be broken down into smaller bits of information that's completely unique and easily retrievable.

Hashing occurs when elements are either stored in, or retrieved from, a **hash table.**

### Hash Tables
A hash table is a kind of data structure that stores each element from a set as a unique key-value pair. The element's index in the table is computed using the hashing process. 

During this process, the element's key is inputted into a **hash function** that computes **hash code**. The hash code is always an integer, even if the key is not, so it can be used to compute the element's index value within the table. 

Hashing makes it possible to instantaneouly locate an element's index, making it possible to add, remove, and locate elements in O(1) time. 

Every value, no matter its initial data type, will be computed into an integer that becomes the key. 

![Chart displaying the steps of the hashing process](../images/hashing_process.jpg)


The power of hash tables is that the element's index in the hash table key is used to determine th
**Non-hashable elements include:**


This kind of key-value pair differs from key-value pairs found in dictionaries because not just any value can be selected as a key in 
sets (especially )

&nbsp;
## Characteristics 
* Not stored in any particular order.
* All elements must be unique.
* Sets can be changed, but only immutable types of elements may be stored in a set.

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
    set_as_is = {'abc'}  # this set contains {'abc'}
    set_new_list = set('abc') # this set contains {'a', 'b', 'c'}
```

### Operations 

#### add(value)


#### remove(value)


#### member(value)


#### size()

in is a Python operation that can check if an element is part of an iterable
