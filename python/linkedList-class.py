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
            new_node.next = self.head  # Connect the new node to the current head using "next" link
            self.head.prev = new_node  # Connect the current head to the new node using the "prev" link
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
            new_node.prev = self.tail  # Connect the new node to the current tail using "prev" link
            self.head.next = new_node  # Connect the current tail to the new node using the "next" link
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
            secondNode = self.head.next  # The head node's next link provides the second node.
            secondNode.prev = None       # Disconnect the second node from the head by setting its prev link to null.
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
            secondToLastNode = self.tail.prev  # The tail node's prev link provides the second to last node.
            secondToLastNode.next = None       # Disconnect the second to last node from the tail by setting its prev link to null.
            self.tail = secondToLastNode       # Now set the tail to the second to last node.