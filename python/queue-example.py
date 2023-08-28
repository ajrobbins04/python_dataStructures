
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
 