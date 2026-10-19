"""
Student: Cesar Lanuza Urbina
Program: Python Intermedio - Sort a doubly linked double-ended queue using Bubble Sort.
"""

# Implement a double-ended queue using doubly linked nodes.
# A double-ended queue allows insertion and removal of values from both ends.
# The implementation uses a Node class to represent each element in the queue,
# with references to the previous and next nodes, enabling traversal in both directions.
# The DoubleEndedQueue class manages the left and right ends of the queue,
# providing methods to push and pop values from either end, as well as a method to print the current state of the queue 
# without modifying it.

# The bubble_sort method sorts the values in ascending order from left to right,
# using the Bubble Sort algorithm. It repeatedly compares adjacent values and swaps them if they are in the wrong order, 
# until the entire queue is sorted. The sorting is done in place, without using any additional data structures, 
# and the method stops early if a complete pass is made without any swaps, indicating that the queue is already sorted.

# The implementation also includes error handling for attempts to pop values from an empty queue,
# raising an IndexError with a descriptive message in such cases.
class Node:
    """Store a value and links to the neighboring nodes."""

    # Each node can be traversed in either direction, allowing for efficient insertion and removal of values from both 
    # ends of the queue.
    def __init__(self, value):
        """Initialize a value and empty links to neighboring nodes."""
        self.value = value
        # Each node can be traversed in either direction.
        self.previous = None
        self.next_node = None


# Implement a double-ended queue using doubly linked nodes.
class DoubleEndedQueue:
    """Implement a double-ended queue using doubly linked nodes."""

    # The double-ended queue allows insertion and removal of values from both ends,
    def __init__(self):
        # Both ends are empty until the first node is added.
        self.left = None
        self.right = None

    # Add a new node at the left end of the queue.
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

    # Add a new node at the right end of the queue.
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

    # Remove and return the leftmost value, raising IndexError if empty.
    def pop_left(self):
        """Remove and return the leftmost value, raising IndexError if empty."""
        if self.left is None:
            raise IndexError("No se puede eliminar un elemento de una cola vacía.")

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

    # Remove and return the rightmost value, raising IndexError if empty.
    def pop_right(self):
        """Remove and return the rightmost value, raising IndexError if empty."""
        if self.right is None:
            raise IndexError("No se puede eliminar un elemento de una cola vacía.")

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

    # Sort values in ascending order from left to right using Bubble Sort.
    def bubble_sort(self):
        """Sort values in ascending order from left to right using Bubble Sort."""
        # Empty queues and single-node queues are already sorted.
        if self.left is None or self.left.next_node is None:
            return

        sorted_boundary = None
        while True:
            current = self.left
            swapped = False

            # Compare adjacent values before the already sorted suffix.
            while current.next_node is not sorted_boundary:
                next_node = current.next_node
                if current.value > next_node.value:
                    # Swap values while preserving both links and queue endpoints.
                    current.value, next_node.value = next_node.value, current.value
                    swapped = True
                current = next_node

            # The largest remaining value reaches its final position each pass.
            sorted_boundary = current
            # Stop early when a complete pass makes no swaps.
            if not swapped:
                break

    # Print all values from left to right without modifying the queue.
    def print_queue(self):
        """Print all values from left to right without modifying the queue."""
        if self.left is None:
            print("La cola está vacía.")
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
    # Build an unsorted queue using insertion at both ends.
    queue = DoubleEndedQueue()
    queue.push_left(20)
    queue.push_left(30)
    queue.push_right(10)
    print("Cola original:")
    queue.print_queue()
    # Sort adjacent values in place, then demonstrate removal at both ends.
    queue.bubble_sort()
    print("Cola ordenada de menor a mayor:")
    queue.print_queue()
    print("Eliminado de la izquierda:", queue.pop_left())
    print("Eliminado de la derecha:", queue.pop_right())
    queue.print_queue()
    print("Último valor eliminado:", queue.pop_left())
    queue.print_queue()
