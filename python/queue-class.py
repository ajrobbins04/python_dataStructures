"""
This example is shown on queues.md as a simple
implementation of a queue class.
"""
class Queue:
    
    def __init__(self):
        """ 
        Create a new queue object that's empty (for now).
        """
        self.queue = []

    def size(self):
        """
        Returns the size of the queue object. Retrieving
        the size has an O(1) performance level.
        """
        return len(self.queue)
        
    
    def is_empty(self):
        """
        Returns True when the queue is empty of any values.
        This operation has an O(1) performance level.
        """
        if len(self.queue) > 0:
            return False
        
        return True

    def enqueue(self, element_value):
        """
        Adds the value of a new queue element to the very
        back of the queue. Enqueue has an O(1) performance
        level.
        """
        self.queue.append(element_value)

    def dequeue(self):
        """
        Per its "First In, First Out" behavior, the
        element value that's at the very front of the queue 
        gets removed by dequeue. The queue stores its values
        in a dynamic array, which gives it O(n) performance.
        """

        # Check if the queue is empty
        if self.is_empty():
            print("The queue is empty.")
            return None
        
        # Remove the element from the queue,
        # and return its value
        value = self.queue.pop(0)
        return value
         
    def print_queue(self):
        """
        Display all the element values in the queue.
        """
        # Check if the queue is empty
        if self.is_empty():
            print("The queue is empty.")
        else:
            # Find the final index value so the last element
            # can be printed without a comma after it.
            size = self.size()
            maxIndex = size - 1
          
            # Print each value found in the queue
            for element in self.queue:
                if element != self.queue[maxIndex]:
                    print(element, end=", ")

                # Print last value
                else:
                    print(element)

                
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