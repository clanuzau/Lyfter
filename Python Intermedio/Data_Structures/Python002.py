"""
Student: Cesar Lanuza Urbina
Program: Pyton Intermedio - Implement a double-ended queue using doubly linked nodes.

Implement a double-ended queue using doubly linked nodes.
A double-ended queue allows insertion and removal of values from both ends.
The implementation uses a Node class to represent each element in the queue,
with references to the previous and next nodes, enabling traversal in both directions.
The DoubleEndedQueue class manages the left and right ends of the queue,
providing methods to push and pop values from either end, as well as a method to print the current state of the queue 
without modifying it.

"""

class Node:
    """Store a value and links to the neighboring nodes."""

    def __init__(self, value):
        self.value = value
        # Each node can be traversed in either direction.
        self.previous = None
        self.next_node = None


class DoubleEndedQueue:
    """Implement a double-ended queue using doubly linked nodes."""

    def __init__(self):
        # Both ends are empty until the first node is added.
        self.left = None
        self.right = None

    def push_left(self, value):
        """Add a new node at the left end of the queue."""
        node = Node(value)
        node.next_node = self.left

        if self.left is None:
            # The first node is both the left and right end.
            self.right = node
        else:
            self.left.previous = node

        self.left = node

    def push_right(self, value):
        """Add a new node at the right end of the queue."""
        node = Node(value)
        node.previous = self.right

        if self.right is None:
            # The first node is both the left and right end.
            self.left = node
        else:
            self.right.next_node = node

        self.right = node

    def pop_left(self):
        """Remove and return the leftmost value, raising IndexError if empty."""
        if self.left is None:
            raise IndexError("Cannot pop from an empty queue.")

        node = self.left
        self.left = node.next_node

        if self.left is None:
            # Removing the only node leaves both ends empty.
            self.right = None
        else:
            self.left.previous = None

        # Detach the removed node from the remaining queue.
        node.next_node = None
        return node.value

    def pop_right(self):
        """Remove and return the rightmost value, raising IndexError if empty."""
        if self.right is None:
            raise IndexError("Cannot pop from an empty queue.")

        node = self.right
        self.right = node.previous

        if self.right is None:
            # Removing the only node leaves both ends empty.
            self.left = None
        else:
            self.right.next_node = None

        # Detach the removed node from the remaining queue.
        node.previous = None
        return node.value

    def print_queue(self):
        """Print all values from left to right without modifying the queue."""
        if self.left is None:
            print("La cola esta vacía.")
            return

        current = self.left
        print()
        print("Izquierdo", end="")
        # Follow node links without storing values in a compound data type.
        while current is not None:
            print(" <-> ", end="")
            print(current.value, end="")
            current = current.next_node
        print(" <-> Derecho")


if __name__ == "__main__":
    # Demonstrate insertion and removal at both ends.
    queue = DoubleEndedQueue()
    queue.push_left(20)
    queue.push_left(10)
    queue.push_right(30)
    queue.print_queue()
    print("Eliminado de la izquierda:", queue.pop_left())
    print("Elimanado de la derecha:", queue.pop_right())
    queue.print_queue()
    print("Ultimo valor eliminado:", queue.pop_left())
    queue.print_queue()
