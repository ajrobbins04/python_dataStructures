
class Queue:
    """
    This is the same queue class that's shown
    to demonstrate the enqueue, dequeue, size, 
    and is_empty operations. The only difference
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
        current order of people in line. 
        """
        # Check if the line is empty
        if self.is_empty():
            print("The line is now empty.")
            return
        
        self.upNext()
        self.show_line()

    def buyTickets(self, num_tickets):
        """
        Updates the line based on how many tickets were 
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
 
########################################
# Example: Movie ticket queue to
# demonstrate how queues can determine 
# the next person in line to buy tickets
# with efficiency
########################################

# Create a queue of moviegoers waiting in line to buy tickets.
ticketLine = Queue()

# Add people to the line
ticketLine.enqueue("James")
ticketLine.enqueue("Rebecca")
ticketLine.enqueue("Dallin")
ticketLine.enqueue("Adelyn")
ticketLine.enqueue("Parker")
ticketLine.enqueue("Brynley")
ticketLine.enqueue("Carson")
ticketLine.enqueue("Janette")

# Display the current line.
ticketLine.show_line()
"""
The current line order: 
1. James
2. Rebecca
3. Dallin
4. Adelyn
5. Parker
6. Brynley
7. Carson
8. Janette
"""

# Update line based on the amount of tickets bought.
ticketLine.buyTickets(5)
"""
James just bought 5 tickets. 
Now it is Brynley's turn to buy tickets.

The current line order: 
1. Brynley
2. Carson
3. Janette
"""

# Two more people join the line.
ticketLine.enqueue("Loren")
ticketLine.enqueue("Noelle")

# Display updated line.
ticketLine.show_line()
"""
The current line order: 
1. Brynley
2. Carson
3. Janette
4. Loren
5. Noelle
"""

# Two final ticket purchases are made.  
# The line updates after each purchase accordingly.
ticketLine.buyTickets(3)
"""
Brynley just bought 3 tickets.
Now it is Loren's turn to buy tickets.

The current line order: 
1. Loren
2. Noelle
"""

ticketLine.buyTickets(2)
"""
Loren just bought 2 tickets.
The line is now empty.
"""