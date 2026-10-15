"""
Student: Cesar Lanuza Urbina
Program: Implement a first-in, first-out queue using linked objects.
"""

# This implementation uses a Node class to store each value and a reference to the next node in the queue.
# The Queue class maintains references to the front and rear nodes, allowing for efficient enqueue and dequeue operations
 

class Node:
    """Store a value and a reference to the next node."""

    # Initialize a new node with the given data and no successor.
    def __init__(self, data):
        # New nodes are not linked to a successor yet.
        self.data = data
        self.next = None


# Implement a first-in, first-out queue using linked objects.
class Queue:
    """Implement a first-in, first-out queue using linked objects."""

    # Initialize an empty queue with no front or rear nodes.
    def __init__(self):
        # Both references are empty until the first node is added.
        self.front = None
        self.rear = None

    # Add a new node to the end of the queue.
    def enqueue(self, data):
        """Add a new node to the end of the queue."""
        new_node = Node(data)

        if self.rear is None:
            # The first node also becomes the front of the queue.
            self.front = new_node
        else:
            # Connect the previous last node to the new node.
            self.rear.next = new_node

        # Update the rear reference after every insertion.
        self.rear = new_node

    # Remove and return the front node, or None if the queue is empty.
    def dequeue(self):
        """Remove and return the front node, or None if the queue is empty."""
        if self.front is None:
            # There is no node to remove from an empty queue.
            return None

        # Save the first node and advance the front to its successor.
        removed_node = self.front
        self.front = removed_node.next

        if self.front is None:
            # Removing the last node leaves both references empty.
            self.rear = None

        # Detach the removed node from the remaining queue.
        removed_node.next = None
        return removed_node

    # Print all values from front to rear, separated by arrows.
    def print_all(self):
        """Print all values from front to rear, separated by arrows."""
        current = self.front

        # Traverse the linked nodes without using built-in containers.
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                # Print a separator only when another node follows.
                print(" -> ", end="")
            current = current.next

        # End the output line, even when the queue is empty.
        print()


if __name__ == "__main__":
    # Run the example only when this file is executed directly.
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    # Show the queue after insertion. Expected output: A -> B -> C
    q.print_all()

    # Remove the first node and show its stored value. Expected output: A
    removed_node = q.dequeue()
    if removed_node is not None:
        print(removed_node.data)

    # Show the remaining queue. Expected output: B -> C
    q.print_all()
