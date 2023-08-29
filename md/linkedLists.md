# Linked Lists
Data structures such as queues and stacks 
**The advantages over dynamic array-based data structures include:**
* Adding and removing elements only has an effect on neighboring elements.
* Elements reaching capacity is not a concern.



## Linked List Performance vs. Dynamic Arrays

### Adding / Removing Elements
Adding or removing elements from the tail of a dynamic array always takes a constant O(1) time. However, the time complexity of these actions increases as the element being acted upon moves closer to the head of the array. Dynamic arrays rely on storing its elements in contiguous memory, so its elements must shift in order to add space for a new element or fill the space vacated by a former element. If an element is added or removed from the head, the performance becomes O(n) since all elements must shift to adjust.

Linked lists **are just as efficient as stacks** because stacks always add elements to *and* remove elements from the tail.

Linked lists **perform better than queues when removing elements,** since queues only remove elements from the head, causing shifts for all the remaining elements. Linked lists and queues are equally efficient when adding elements because queues add to the tail.

Note that the performance disadvantage of removing elements from the head of a queue can be solved when a **deque** is implemented instead of a queue. 

The deque (pronounced *"deck"*) behaves 

### Retrieving Elements
When searching for an element without knowing its index, then both linked lists and dynamic arrays must traverse through every element in O(n) time until the element is found (if it is indeed found).

However, dynamic arrays **outperform linked lists when the index is known.** In this case, dynamic arrays can retrieve the desired element in O(1) time because its elements are stored in contiguous memory blocks, so there is no need to traverse through them. Linked lists, on the other hand, must still traverse through every element in O(n) time because its elements are stored in scattered memory addresses. There is no possible way to locate an element unless the linked list's nodes are traversed one by one. 

## Linked List Implementation

### Creating a Linked List

### Inserting at the Head

(include special case if linked list is empty)

### Inserting at the Tail

### Inserting in the Middle

### Element Access

### Element Removal

## Linked List Operations