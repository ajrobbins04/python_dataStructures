class Waitlist_Queue:
    """
    Every waitlist object is a queue that stores library card barcodes.
    These barcodes are unique identifiers which each correspond to a
    person's library account
    """ 
    def __init__(self):
        """ 
        Create a new queue object that's empty (for now).
        """
        self.queue = []

    def size(self):
        """
        Returns the size of the waitlist queue. 
        This operation has an O(1) performance level.
        """
        return len(self.queue)
        
    def is_empty(self):
        """
        Returns True when the waitlist queue is empty.
        This operation has an O(1) performance level.
        """
        if len(self.queue) > 0:
            return False
        
        return True

    def enqueue(self, barcode):
        """
        Adds a new person (as represented by their
        library card) to the back of the waitlist.  
        This operation has an O(1) performance level.
        """
        self.queue.append(barcode)

    def dequeue(self):
        """
        Remove person from the front of the waitlist.
        Since the queue's values are stored in a 
        dynamic array, it has O(n) performance.
        """
        # Check if the waitlist queue is empty
        if self.is_empty():
            print("The waitlist is empty")
            return None
        
        # Remove the barcode from the queue,
        # and return its value
        barcode = self.queue[0]
        del self.queue[0]
        return barcode
    

 
 
class Book:
    """
    Each object created by this class will represent a collection of either one 
    book or multiple copies of the same book within a library system. Every book 
    will have its own waitlist queue so library patrons can wait their turn to 
    borrow it if it is currently checked out. In instances where there are multiple 
    copies of the same book, then all theses copies will share the same waitlist.
    """
 
    def __init__(self, title, inventory, waitlist: Waitlist_Queue):
        """ 
        Create a new book object. For the purpose of this
        example, the book's attributes do not need to be
        thorough (no author, isbn, etc).
        """
        self.title = title

        # At instantiation, inventory represents all the 
        # copies of a book in the library system. The 
        # value will be updated as copies are being
        # checked out and turned in.
        self.inventory = inventory

        # Every Book object has a waitlist attribute, which
        # is an object from the Waitlist_Queue class.
        self.waitlist = waitlist
       
    
    def is_available(self):
        """
        Check if the book is currently available
        to check out.
        """

        if self.inventory == 0:
            return False
        else:
            return True
        
    def add_waitlist(self, barcode):
        """
        Add the barcode of a person's library card 
        to the waitlist of a book if the book is  
        currently unavailable.
        """
        self.waitlist.enqueue(barcode)

    def check_out(self, barcode):
        """
        A book can be checked out if it is readily 
        available. Sometimes this will involve 
        advancing through a waitlist, but not
        always.

        Let's just assume that any person
        who wants to borrow a certain book is
        willing to wait for it when necessary.
        """
        # book can be borrowed right away.
        if self.inventory > 0:
            self.inventory -= 1
        else:
            self.add_waitlist(barcode)

    def return_book(self):
        """
        When a book gets returned to the library, this
        method must check if anyone is currently on that 
        book's waitlist. If yes, then the book is not 
        added back into the library inventory. Instead, it
        goes to whomever is at the top of the waitlist.
        """
        if self.waitlist.is_empty():
            self.inventory += 1
        
        # Remove whomever is at the front
        # of the waitlist since the returned
        # book is checked out to him/her.
        else:
            self.waitlist.dequeue()

    def print_waitlist(self):
        """
        Display all the card barcodes that are stored
        in the waitlist. They will be ranked according
        to their position in the queue (1 would be at
        the very front).
        """
        
        # Check if the waitlist queue is empty
        if self.waitlist.is_empty():
            print("The waitlist is empty.")
        else:
            # Will iterate through the barcodes starting with
            # the one at the front, so it will be ranked as 1.
            rank = 1

            # List each library card barcode that's stored in the waitlist queue
            print(f"Here is the current waitlist for '{self.title}':\n")
            for barcode in self.waitlist.queue:
                print(f"\t{rank}. barcode #{barcode}")
                rank += 1
 
    def display_status(self):
        """
        This method lets us know the status of a book. Namely, is it
        available to be checked out, and if it is checked out, then 
        what is the status of its waitlist?
        """
        if self.inventory > 0:
            print(f"\n'{self.title}' is currently available to check out.")

        elif self.inventory == 0 and self.waitlist.is_empty():
            print(f"\n'{self.title}' is currently unavailable to check out, but its waitlist is empty.")

        else:
            num = self.waitlist.size()
            print(f"\n'{self.title}' is currently unavailable to check out. There are {num} people on the waitlist.\n")
            self.print_waitlist()
 
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