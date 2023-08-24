![Image of Waldo from "Where's Waldo"](images/sets_intro.jpg)

# Sets
For the record, sets really would be the data structure that crushes the competition in "Where's Waldo". But, Sets are more properly characterized in technology as the data structure that's great at determining membership.
 
Interestingly, sets are able to exceed at being able to determine whether it is storing a particular data value  even though it never attempts to sort its incoming data.  

**Sets are highly efficient at sorting thanks to a technique called hashing.**

## Hashing
Hashing is a process that has a lot of different applications in technology today, including the fields of cybersecurity and database management. While its actual implementation details may differ based on the application, hashing always provides a means by which information can be broken down into smaller bits of information that's completely unique and easily retrievable. 

In Python, hashing is used to convert build a **hash table.** 

### Hash Tables
Hash tables provide a way for data to be stored as unique key-value pairs. are essentially built by entering any valid input into a hash function, which then breaks it down into a new value. That value becomes the input value's key, which is a unique identifier. 

This kind of key-value pair differs from key-value pairs found in dictionaries because not just any value can be selected as a key in 
sets (especially )

![Chart displaying the steps of the hashing process](images/hashing_process.jpg)

## Essential Set Characteristics to Understand  
* Sets are not stored in any particular order.
* Set elements must be unique.
* Sets can be changed, but only immutable types of elements  
may be stored in a set.



## Implementing Sets in Python
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