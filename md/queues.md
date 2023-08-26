![Cartoon image of people standing in a waiting queue](../images/queue_intro.webp)

# Queues

A queue is characterized by its **First In, First Out (FIFO) behavior**. This means that data
is always added to the back (tail) of a queue, and it can only be removed once it has finally 
advanced to the very front (head) of the queue. 

**Thus, the order that data leaves a queue will be the same order in which it entered the queue.**

&nbsp;
## Queues in the Real World
Compared to other data structures, a queue's behavior is relatively simple and easy to
understand from a real-world perspective. When data enters a queue, it is just taking its
place to wait at the back of a line like its human counterparts do all the time. The most
obvious difference is that data is perfectly patient when waiting its turn (which is a far cry 
from what transpires at the DMV), so data never tries to "cut" when waiting its turn to exit
the queue, nor does it try to leave the queue early.

 &nbsp;
## Queues in Technology
Technology utilizes queues extensively. Queues provide structure and order when automated tasks 
must be carried out, and they provide a way for resources to be shared without overwhelming 
and crashing a system. 

### Printer Queues
Way back when printers were prohibitively expensive, it was common practice for many users
to all share the same printer. The printer would end up receiving tons of print job requests,
so it would organize these requests into a queue to methodically print every request.

![Illustration depicting how a printer queue works](../images/printer_queue.png)
Personal printers may be much easier to purchase nowadays, but it still accomplishes all its
printing tasks by starting with the request that was received first, then the second request,
followed by the third request, and so on.

**Additional Examples of Queues Include:**
* **CPU scheduling**, in which the operating system determines which process will be 
run by the CPU based on its place in a queue. Some higher priority processes do get to
skip over others, but "first come, first served" queues are typically used during times 
when mostly routine maintenance processes are in the queue.
* **Company call centers**, which determine which customer gets to speak to a representative
next based on how long they've been in the waiting queue.
* **Websites**, which can't handle all HTTP requests at once. It serves each request using 
queues, which helps ensure that website response times aren't sluggish.

&nbsp;
## Queue Implementation
Queues can be implemented in many different coding languages in addition to Python, including 
C, C++, and Java. Even though the actual implementation details vary based on which coding language is being used, the set of operations associated with queues will remain the same.

In Python, queues are **implemented using lists**:

![example of a queue object in Python being instantiated using a list](../images/queue_instantiate.png)

Lists in Python are **dynamic arrays**.

This means a queue's data will be stored in memory addresses that are contiguous to each other. This will play a large role in determining the
performance level of each operation.

&nbsp;
### Operations:

#### enqueue(element_value)
* Adds a new element to the back of the queue. 
* Is implemented using the append() list method.
* Performance Level: **O(1)** 
    * The input size does not affect the amount of time taken to execute 
    enqueue. Appending to the tail always occurs in one step.

![example of an enqueue operation implemented in Python](../images/queue_enqueue.png)

#### dequeue()
* Removes an element from the front of the queue. 
* Can be implemented using either the pop() list method or the del operator.
* Performance Level: **O(n)**
    * Removing the element at index 0 will result in a shift where all the 
    other elements move up the queue by one index value closer to the front.
    * Every element must be iterated through to perform this shift.

![example of 2 dequeue operation approaches implemented in Python](../images/queue_dequeue-2.png)

#### deque (a quick sidenote)
* The more efficient alternative to dequeue.
* Stands for "double-ended queue".
* Deque is a Python library that implements queues using linked lists instead of lists
that are dynamic arrays.
* By using linked lists, operations like dequeue become more efficient because there is no huge shift of all the elements after dequeue when they aren't located in contiguous memory addresses.

#### size()
* Provides the queue's size.
* Is implemented using the len() list method.
* Performance Level: **O(1)**
    * len() does not require a loop to count up the size of a list.

![example of the size operation implemented in Python](../images/queue_size.png)

#### is_empty()
* Checks if the queue has no elements. 
* The len() method is used to get the queue's size, and is_empty()
returns True whenever the size is 0.
* Performance Level: **O(1)**
    * len() does not require a loop to count up the size of a list.

![example of the is_empty operation implemented in Python](../images/queue_is_empty.png)


The examples for all these operations can be used together to create a simple,
functional queue class - as shown [here](python/queue-class.py) 

```python
                
########################################
# Check that the queue operations
# work as expected. 
########################################

# Create a queue.
my_queue = Queue()

# Add 5 values to the queue using enqueue.
my_queue.enqueue("first")
my_queue.enqueue("second")
my_queue.enqueue("third")
my_queue.enqueue("fourth")
my_queue.enqueue("fifth")

# Prints "first, second, third, fourth, fifth"  
# since values are added to the back of the queue.
my_queue.print_queue() 

# Remove 2 values from the queue using dequeue.
my_queue.dequeue()
my_queue.dequeue()

# Prints "third, fourth, fifth"
# since values are removed from the front.
my_queue.print_queue()

# Add "first" and "second" to the back of the 
# queue again.
my_queue.enqueue("first")
my_queue.enqueue("second")

# Prints "third, fourth, fifth, first, second"
my_queue.print_queue()
        
```

&nbsp;
## Example: Movie Ticket Queue
This example depicts a line to buy tickets at a movie
theater. Each person in line must wait their turn to 
but tickets, which is a very clear case of "First In,
First Out" queue behavior. By using queues, this example
is able to determine whose turn it is to buy tickets. 
Except, one cannot assume each person in the queue will
simply buy one ticket for themselves. Oftentimes people
attending the movies as a group will stand in line together,
then one member of the group makes the ticket purchases for 
everyone. This will affect how the queue determines who is
next in line to buy tickets.

The .py version of this example can be found [here](python/queue-example.py)

```python
class Queue:
    """
    This is the same queue class that's shown
    in the previous example. The only difference
    is that a few things were renamed to better
    reflect the scenario and additional methods 
    were added to increase functionality.
    """

    def __init__(self):
        """ 
        Create an empty queue called line.
        """
        self.line = []

    def size(self):
        """
        Returns the size of the customer line.  
        """
        return len(self.line)
        
    def is_empty(self):
        """
        Returns True when the customer line is empty.
        """
        if len(self.line) > 0:
            return False
        
        return True

    def enqueue(self, person):
        """
        Adds a new person to the very back of the line.
        """
        self.line.append(person)

    def dequeue(self):
        """
        Removes a person from the front of the line.
        """
        # Check if the line is empty
        if self.is_empty():
            print("The line is empty.")
            return None
        
        # Remove the person at the front of 
        # the line.
        person = self.line[0]
        del self.line[0]
        return person

    def upNext(self):
        """
        Displays whose turn it is to buy tickets.
        """
        print(f"Now it is {self.line[0]}'s turn to buy tickets.\n")

    def show_line(self):
        """
        Displays all the people in the ticket line.
        """
        # Check if the line is empty
        if self.is_empty():
            print("The line is empty.")
        else:
            # Represents the front of the line.
            position = 1
            
            # Display the order of people waiting
            # in line.
            print("The current line order: ")
            for person in self.line:
                print(f"{position}. {person}")
                position += 1

            print("\n")

    def display_line_stats(self):
        """
        Displays who gets to purchase tickets next, along with the 
        current order of people in line. This method gets called 
        after a ticket purchase is made.
        """
        # Check if the line is empty
        if self.is_empty():
            print("The line is now empty.")
            return
        
        self.upNext()
        self.show_line()

    def buyTickets(self, num_tickets):
        """
        Oftentimes movie goers will stand in line together,
        then one person purchases the tickets for everyone
        in their group. Thus, the next person to buy tickets
        won't always be the second person in line. This method
        updates the line based on how many tickets were 
        purchased by the person at the front of the line.
        """
        # Check if the line is empty.
        if self.is_empty():
            print("The line is currently empty.")
            return

        # Display who is purchasing tickets, along
        # with the number of tickets being purchased.
        print(f"{self.line[0]} just bought {num_tickets} tickets.")

        # The amount of people who leave the line is 
        # based on the number of purchased tickets.
        for customers in range(num_tickets):
            self.dequeue()
    
        # Show new line stats following ticket purchase
        self.display_line_stats()
 

# Create a queue of moviegoers waiting in line to buy tickets.
ticketLine = Queue()

# Add people to the line.
ticketLine.enqueue("James")
ticketLine.enqueue("Rebecca")
ticketLine.enqueue("Dallin")
ticketLine.enqueue("Adelyn")
ticketLine.enqueue("Parker")
ticketLine.enqueue("Brynley")
ticketLine.enqueue("Carson")
ticketLine.enqueue("Janette")

# Display the order of everyone in line.
ticketLine.show_line()

# People in line will move forward based
# on the amount of tickets bought.
ticketLine.buyTickets(5)

# Two more people joined the line,
# so display the new order of everyone in
# line again.
ticketLine.enqueue("Loren")
ticketLine.enqueue("Noelle")
ticketLine.show_line()

# More ticket purchases are made. The line
# will adjust itself accordingly.
ticketLine.buyTickets(3)
ticketLine.buyTickets(2)
```

### The output of this example will display: 
The current line order: 
1. James
2. Rebecca
3. Dallin
4. Adelyn
5. Parker
6. Brynley
7. Carson
8. Janette

James just bought 5 tickets. 
Now it is Brynley's turn to buy tickets.

The current line order: 
1. Brynley
2. Carson
3. Janette

The current line order: 
1. Brynley
2. Carson
3. Janette
4. Loren
5. Noelle

Brynley just bought 3 tickets.
Now it is Loren's turn to buy tickets.

The current line order: 
1. Loren
2. Noelle

Loren just bought 2 tickets.
The line is now empty.

&nbsp;
## Digging Deeper: Queues vs. Stacks 
One of the interesting things about queues is that it has a sibling data structure, so to
speak, called stacks. Stacks, like queues, are implemented in Python using lists.

While queues are the main focus of this lesson, it is worth bringing up stacks because 
understanding their similarities and differences comes in handy when trying to decide
between using a queue or a stack in a program. 

### Similarities
* As dynamic arrays, queues and stacks are both stored in contiguous memory addresses.
* Their elements can be accessed easily.
* Queues and stacks have no fixed sizes. They can grow in size as more elements are added.
* A user may have to create a larger queue or stack if they run out of memory, 
but this does not occur frequently.
* Neither one inserts or removes data from somewhere in between the first and last indices.

### Differences
* Queues use First In, First Out (FIFO) behavior, whereas stacks use Last In, First Out (LIFO) behavior.
* With LIFO, data gets added *and* removed from the end of the list. The data element that was most recently 
added to a stack will be the first to leave it. 
* Think of stacks like adding and removing ceramic plates from a whole stack of breakable plates. In order 
to avoid a very shattering case of plate extinction, plates are stored by stacking each new plate top of 
each other, and they are retrieved by selecting whichever plate is currently on the very top of the stack.

### Can data be added or removed from somewhere in the middle of Queues and/or Stacks?
Technically speaking, additional code can be written to make these things possible. However,  
only being able to add data at the tail and remove data at the head are characteristics that
define a queue. Likewise, only being able to add and remove data from the tail is what defines
a stack. So, once a queue or a stack class breaks out of their defined behaviors, then they aren't
necessarily considered queues or stacks any more.

&nbsp;
## Final Problem to Solve: Library Book Waitlist Queue
To practice using a queue in a program, try designing a waitlist queue for a library
system. This program is just a simplified version, so it doesn't need to take all 
aspects of an actual library waitlist into consideration.

### Specifications

**Design a class called Waitlist_Queue:**
* The only attribute that a Waitlist_Queue object requires is a list called "queue".
* The queue attribute will store library card barcodes. 
    * Library systems don't place people on waitlists using their names. They need a more unique 
    identifier, which is why the barcode from a person's library card is used instead.  
* Only implement the operations of a queue as methods for this class. No "bonus" print method is necessary
(that will be included in the Book class).

**Design another class called Book:**
* A Book object will have a title, an inventory number, and a Waitlist_Queue object called "waitlist"
as its attributes.
* Implement the is_available() method to check if a book is currently available to check out.
* Implement the add_waitlist() method to add the barcode of a person's library card to a book's waitlist 
if it is unavailable.
* Implement the check_out() method, which either "checks out" a book by adjusting its inventory size,
or it places someone (using their library card barcode) onto the book's waiting list when they attempt
to check out a currently unavailable book.
* Implement the return_book() method so a book gets added back into the inventory if its waitlist is
empty, or it "gives" the book to the next person on the waitlist.
* Implement the print_waitlist() method to show all the card barcodes that are stored in a book's waitlist.
Rank each barcode according to its position in the waitlist (1 would be at the head).
* Implement the display_status() method to provide updates on a book's status.
    * Is the book available to be checked out?
    * If it isn't available, then is there currently a waitlist?
    * If there is a waitlist, then what is its size? How is the waitlist currently ranked?


Trying to solve this problem from scratch is encouraged. However, if additional
guidance if needed, try solving [this version of the problem instead.](python/queue-solution.py)

The full solution of this problem can be found [here](python/queue-solution.py)


### Once your program is complete, test the accuracy of your code by running these tests: 
```python
# Create 4 waitlists using the Waitlist_Queue class and 4
# book collections using the Book class. Every book collection 
# receives one waitlist as an attribute.

waitlist1 = Waitlist_Queue()
book1 = Book("Structure and Interpretation of Computer Programs", 2, waitlist1)

waitlist2 = Waitlist_Queue()
book2 = Book("Programming Pearls", 1, waitlist2)

waitlist3 = Waitlist_Queue()
book3 = Book("The Pragmatic Programmer: Your Journey to Mastery", 2, waitlist3)

waitlist4 = Waitlist_Queue()
book4 = Book("Code Simplicity: the Fundamentals of Software", 3, waitlist4)


print("\n=========== TEST 1 ===========")
# There are 2 copies of book1. Check that the waitlist
# grows once the book's demand is greater than
# its supply.
 
book1.check_out(1111)
book1.check_out(2222)
book1.check_out(3333)
book1.check_out(4444)

print("*** 4 attempts were made to check out book1's 2 copies ***")
book1.display_status()
"""
'Structure and Interpretation of Computer Programs' is currently unavailable to check out. There are 2 people on the waitlist.

Here is the current waitlist for 'Structure and Interpretation of Computer Programs':

    1. barcode #3333
    2. barcode #4444
""" 


print("\n=========== TEST 2 ===========")
# There is only 1 copy of book2. Confirm that the
# status of book2 changes once it is checked out 
# to reflect that it is unavailable for check-out.
book2.check_out(1001)

print("*** The only copy of book2 was checked out ***")
book2.display_status()
"""
'Programming Pearls' is currently unavailable to check out, but its waitlist is empty.
"""

# Confirm that book2's status switches to being
# available once it is returned.
book2.return_book()

print("\n*** The only copy of book2 was returned ***")
book2.display_status()
"""
'Programming Pearls' is currently available to check out.
"""


print("\n=========== TEST 3 ===========")
# Let's check that the waitlist queue behaves as
# expected when more than one book becomes available.

# There are 2 copies of book3.
book3.check_out(1122)
book3.check_out(3344)
book3.check_out(5566)
book3.check_out(7788)
book3.check_out(9911)
 
print("\n*** 5 attempts were made to check out the 2 copies of book3 ***")
book3.display_status()
"""
'The Pragmatic Programmer: Your Journey to Mastery' is currently unavailable to check out. There are 3 people on the waitlist.

Here is the current waitlist for 'The Pragmatic Programmer: Your Journey to Mastery':

    1. barcode #5566
    2. barcode #7788
    3. barcode #9911
"""
 
# Confirm that, once 2 copies get returned, they are
# checked out to the 1st and 2nd waitlisters.  
book3.return_book()
book3.return_book()

print("\n*** The 2 copies of book3 were returned ***")
book3.display_status()
"""
'The Pragmatic Programmer: Your Journey to Mastery' is currently unavailable to check out. There are 1 people on the waitlist.

Here is the current waitlist for 'The Pragmatic Programmer: Your Journey to Mastery':

    1. barcode #9911
"""


print("\n=========== TEST 4 ===========")
# Let's exercise the waitlist queue a little more 
# just to further confirm that it works as expected.

# There are 3 copies of book4.
book4.check_out(1110)
book4.check_out(2221)
book4.check_out(3332)
book4.check_out(4443)


print("\n*** 4 attempts were made to check out the 3 copies of book4 ***")
book4.display_status()
"""
'Code Simplicity: the Fundamentals of Software' is currently unavailable to check out. There are 1 people on the waitlist.

Here is the current waitlist for 'Code Simplicity: the Fundamentals of Software':

    1. barcode #4443
"""

# Return all 3 copies (one should automatically go to the waitlister).
book4.return_book()
book4.return_book()
book4.return_book()

 
print("\n*** All 3 copies of book4 were returned (although only 2 should end back up in inventory) ***")
book4.display_status()
"""
'Code Simplicity: the Fundamentals of Software' is currently available to check out.
"""

book4.check_out(5554)
book4.check_out(6665)

# This result confirms that 2, and not 3, copies got added to inventory after 
# the previous step.
print("\n*** 2 copies got checked out again. ***")
book4.display_status()
"""
'Code Simplicity: the Fundamentals of Software' is currently unavailable to check out, but its waitlist is empty.
"""
```
 
## [Click Here](queue_attributions.md) to view all attributions for this queue tutorial.
