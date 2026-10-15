"""
Student: Cesar Lanuza Urbina
Program: A doubly linked list is a sequence of nodes that can be traversed in both directions.
"""

# Each node contains a value and references to both its predecessor and successor nodes.
# This implementation provides methods to append, prepend, delete, and print the list in both directions.
# The example usage demonstrates the functionality of the doubly linked list by appending, prepending, deleting nodes, 
# and printing the resulting list after each operation.
 

# A doubly linked list is a sequence of nodes that can be traversed in both directions.
class Node:
    """Store a value and references to the previous and next nodes."""

    def __init__(self, data):
        # A new node starts without neighboring nodes.
        self.data = data
        self.previous = None
        self.next = None


# Implement a doubly linked list with basic operations.
class DoublyLinkedList:
    """Represent a linked list that can be traversed in both directions."""

    # Initialize an empty doubly linked list with no head or tail nodes.
    def __init__(self):
        # An empty list has neither a first node nor a last node.
        self.head = None
        self.tail = None

    # Add a new node at the end of the list.
    def append(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        new_node.previous = self.tail

        if self.tail is None:
            # The first node also becomes the head of the empty list.
            self.head = new_node
        else:
            # Link the previous tail to the new node in the forward direction.
            self.tail.next = new_node

        self.tail = new_node

    # Add a new node at the beginning of the list.
    def prepend(self, data):
        """Add a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head

        if self.head is None:
            # The first node also becomes the tail of the empty list.
            self.tail = new_node
        else:
            # Link the previous head to the new node in the backward direction.
            self.head.previous = new_node

        self.head = new_node

    # Remove the first node containing the specified value, if it exists.
    def delete(self, data):
        """Remove the first matching node and return whether it was found."""
        current = self.head

        # Search from the head to find the first occurrence of the value.
        while current is not None:
            if current.data == data:
                if current.previous is None:
                    # Removing the first node requires updating the head.
                    self.head = current.next
                else:
                    current.previous.next = current.next

                if current.next is None:
                    # Removing the last node requires updating the tail.
                    self.tail = current.previous
                else:
                    current.next.previous = current.previous

                # Detach both links after reconnecting the neighboring nodes.
                current.previous = None
                current.next = None
                return True

            current = current.next

        # Leave the list unchanged when the value is absent.
        return False

    # Print all values from head to tail, separated by arrows.
    def print_forward(self):
        """Print all values from head to tail, separated by arrows."""
        current = self.head

        # Follow the next reference to traverse the list forward.
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next

        # Finish the line even when the list is empty.
        print()

    # Print all values from tail to head, separated by arrows.
    def print_backward(self):
        """Print all values from tail to head, separated by arrows."""
        current = self.tail

        # Follow the previous reference to traverse the list backward.
        while current is not None:
            print(current.data, end="")
            if current.previous is not None:
                print(" -> ", end="")
            current = current.previous

        # Finish the line even when the list is empty.
        print()


if __name__ == "__main__":
    # Run the example only when this file is executed directly.
    print()
    dll = DoublyLinkedList()

    # Append three values and display both traversal directions.
    dll.append("A")
    dll.append("B")
    dll.append("C")
    dll.print_forward()   # A -> B -> C
    dll.print_backward()  # C -> B -> A

    print()
    # Prepend a value and verify its position in both directions.
    dll.prepend("X")
    dll.print_forward()   # X -> A -> B -> C
    dll.print_backward()  # C -> B -> A -> X

    print()
    # Delete the first matching value and display the remaining nodes.
    dll.delete("B")
    dll.print_forward()   # X -> A -> C
    dll.print_backward()  # C -> A -> X

    print()
