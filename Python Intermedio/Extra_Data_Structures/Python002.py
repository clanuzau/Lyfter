""" 
Student: Cesar Lanuza Urbina
Program: A simple implementation of a singly linked list in Python.
"""
# This implementation uses a Node class to store each value and a reference to the next node in the list. 
# The LinkedList class maintains a reference to the head node, allowing for efficient insertion and 
# deletion operations at both ends of the list. 
# The list can be traversed to print all values in order, and nodes can be removed by value, with only the first matching
# node being deleted. The implementation includes methods to insert nodes at the front and back of the list, 
# delete nodes by value, and print all values in the list. 
# The example usage demonstrates the functionality of the linked list by inserting and deleting nodes and printing 
# the resulting list after each operation.    
 

# A simple implementation of a singly linked list in Python.
class Node:
    """Store a value and a reference to the next node."""

    # Initialize a new node with the given data and no successor.
    def __init__(self, data):
        # A new node starts without a successor.
        self.data = data
        self.next = None


# Implement a singly linked list with basic operations.
class LinkedList:
    """Represent a singly linked list of nodes."""

    # Initialize an empty linked list with no head node.
    def __init__(self):
        # An empty list has no first node.
        self.head = None

    # Insert a new node at the beginning of the list.
    def insert_front(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        # Link the new node to the previous head before replacing it.
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end of the list.
    def insert_back(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            # The first inserted node becomes the head of an empty list.
            self.head = new_node
            return

        # Find the last node and attach the new node to it.
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Remove the first node containing the specified value, if it exists.
    def delete(self, data):
        """Remove the first matching node and return whether it was found."""
        previous = None
        current = self.head

        # Search from the head so only the first matching value is removed.
        while current is not None:
            if current.data == data:
                if previous is None:
                    # Removing the head makes its successor the new head.
                    self.head = current.next
                else:
                    # Bypass the matching node while preserving the remaining links.
                    previous.next = current.next

                # Detach the removed node and stop after the first match.
                current.next = None
                return True

            previous = current
            current = current.next

        # An empty list or a missing value leaves the list unchanged.
        return False

    # Print all values in order, separated by arrows.
    def print_all(self):
        """Print all values in order, separated by arrows."""
        current = self.head
        while current is not None:
            print(current.data, end="")
            # Add a separator only when another node follows.
            if current.next is not None:
                print(" -> ", end="")
            current = current.next

        # End the output line, including when the list is empty.
        print()


if __name__ == "__main__":
    # Run the example only when this file is executed directly.
    print()
    ll = LinkedList()

    # Insert at the front. Expected output: 20 -> 10
    ll.insert_front(10)
    ll.insert_front(20)
    ll.print_all()

    # Insert at the back. Expected output: 20 -> 10 -> 30
    ll.insert_back(30)
    ll.print_all()

    # Delete the first node containing 10. Expected output: 20 -> 30
    ll.delete(10)
    ll.print_all()

    print()
