class LinkedList:
    """
    Implements the doubly-linked list data structure.
    This class has an inner class, Node, that will be
    used to instantiate every node contained in the
    doubly-linked list. 
    """

    class Node:
        """
        Every node contains data and links to the
        "previous" and "next" nodes.
        """

        def __init__(self, data):
            """
            Initializes the node with the provided
            data. Initially the links are unknown,
            so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list. 
        """
        self.head = None
        self.tail = None
    
    def insert_head(self, value):
        """
        Inserts a new node at the head (front)
        of the linked list.
        """

        # Create the new node
        new_node = LinkedList.Node(value)

        # If the list is empty, then point the
        # head and the tail to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # If the the list is not empty, then only
        # self.head will be affected by the insertion.
        else:
            new_node.next = self.head  # Connect the new node to the current head using its 'next' link
            self.head.prev = new_node  # Connect the current head to the new node using its 'prev' link
            self.head = new_node       # Now set the head equal to the new node

    def insert_tail(self, value):
        """
        Inserts a new node at the tail (back) 
        of the linked list.
        """

        # Create the new node
        new_node = LinkedList.Node(value)

        # If the list is empty, then point the
        # head and the tail to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # If the the list is not empty, then only
        # self.tail will be affected by the insertion.
        else:
            new_node.prev = self.tail  # Connect the new node to the current tail using its 'prev' link
            self.tail.next = new_node  # Connect the current tail to the new node using its 'next' link
            self.tail = new_node       # Now set the tail equal to the new node

    def remove_head(self):
        """
        Removes the first node of the linked list.
        """
        # If there is only one node in the list, then 
        # it represents the head and the tail. Both attributes
        # will need to be set to null to remove it.
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # Removal only applies to the head when there's more than one node.
        else:
            secondNode = self.head.next  # The head node's 'next' link provides the second node.
            secondNode.prev = None       # Disconnect the second node from the head by setting its 'prev' link to null.
            self.head = secondNode       # Now set the head to the second node.

    def remove_tail(self):
        """
        Removes the last node of the linked list.
        """
        # If there is only one node in the list, then 
        # it represents the head and the tail. Both attributes
        # will need to be set to null to remove it.
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # Removal only applies to the tail when there's more than one node.
        else:
            secondToLastNode = self.tail.prev  # The tail node's 'prev' link provides the second to last node.
            secondToLastNode.next = None       # Disconnect the second to last node from the tail by setting its 'prev' link to null.
            self.tail = secondToLastNode       # Now set the tail to the second to last node.
    
    def insert_after(self, value, new_value):
        """
        Inserts 'new_value' after the first occurence
        of 'value' in the linked list.
        """
        # Begin searching for the node that holds 
        # 'value' at the head of the list.
        curr_node = self.head

        while curr_node is not None:
            if curr_node.data == value:
                # if current node is also the tail node, then call insert_tail().
                if curr_node == self.tail:
                    self.insert_tail(new_value)
                # If value is found in any other current node, then it will create
                # and insert the new node at the next node.
                else: 
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr_node   # Connect the new node's 'prev' link to the current node.
                    next_node = curr_node.next  # Get the next node after current node from its 'next' link.
                    new_node.next = next_node   # Connect the new node's 'next' link to the next node.
                    next_node.prev = new_node   # Connect the next node's 'prev' link to the new node.
                    next_node = new_node        # Set the next node equal to the new node.
                
                # Can exit the function once new node is inserted.
                return 
            
            # Go to the next node to search for 'value'.
            curr_node = curr_node.next

    def remove(self, value):
        """
        Removes the first node found that contains 'value'.
        """
        # Begin searching for the node that holds 
        # 'value' at the head of the list.
        curr_node = self.head

        # If the head node contains 'value',
        # then call remove_head()
        if curr_node.data == value:
            self.remove_head()

        else:
            # Search for value until it is found,
            # or the end of the list is reached.
            while curr_node is not None:
                if curr_node.data == value:
                    # If the tail node contains 'value',
                    # then call remove_tail()
                    if curr_node == self.tail:
                        self.remove_tail()

                    # If value is found in any other current node,
                    # then remove the current node.
                    else:
                        """
                        The following two lines of code could be used
                        instead of the code on lines 176 - 180:

                        curr_node.next.prev = curr_node.prev
                        curr_node.prev.next = curr_node.next

                        However, the extra lines of code are used to make the
                        action of removing the current node less convoluted.
                        """
                        prev_node = curr_node.prev  # Get the prev node before current node from its 'prev' link.
                        next_node = curr_node.next  # Get the next node after current node from its 'next' link.
                        
                        prev_node.next = curr_node.next # Set the previous node's 'next' link to the curent node's 'next' link.
                        next_node.prev = curr_node.prev # Set the next node's 'prev' link to the current node's 'prev' link.
                    
                    # Exit out of function once current node is removed.
                    return
                
                # Go to the next node to search for 'value'.
                curr_node = curr_node.next

    def __iter__(self):
        """
        Iterates forward through the linked list.
        """
        current = self.head  # Start at the head for a forward iteration.

        while current is not None:
            yield current.data      # Provide each item to the user.
            current = current.next  # Move forward to the next node.

    def __reverseIter__(self):
        """
        Iterates backward through the linked list.
        """
        current = self.tai  # Start at the tail for a backward iteration.

        # Iterate backwards until reaching the head node's 'prev' link.
        while current != self.head.prev:
            yield current.data      # Provide each item to the user.
            current = current.prev  # Move backward to the previous node.

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linked list: ["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
    

print("\n=========== PROBLEM 1 TESTS ===========")
ll = LinkedList()
ll.insert_tail(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]
ll.insert_tail(0)
ll.insert_tail(-1)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0, -1]

print("\n=========== PROBLEM 2 TESTS ===========")
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0]
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]

print("\n=========== PROBLEM 3 TESTS ===========")
ll.insert_after(3, 3.5)
ll.insert_after(5, 6)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(-1)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(3)
print(ll) # linkedlist[5, 6, 4, 3.5, 2, 2, 2, 1]
ll.remove(6)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2, 1]
ll.remove(1)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(7)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(5)
print(ll) # linkedlist[4, 3.5, 2, 2, 2]
ll.remove(2)
print(ll) # linkedlist[4, 3.5, 2, 2]




print("\n=========== PROBLEM 5 TESTS ===========")
print(list(reversed(ll)))  # [10, 10, 3.5, 100]