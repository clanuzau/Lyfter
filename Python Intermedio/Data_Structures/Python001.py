"""
Student: Cesar Lanuza Urbina
Program: Pyton Intermedio - Implement a last-in, first-out stack using linked nodes.
"""

# Implement a last-in, first-out stack using linked nodes.
class Node:
    """Store a value and a reference to the next node."""

    # Initialize a node with a value and an optional reference to the next node.
    def __init__(self, value, next_node=None):
        # Link this node to the node immediately below it.
        self.value = value
        self.next_node = next_node


class Stack:
    """Implement a last-in, first-out stack using linked nodes."""

    # Initialize an empty stack with no top node.
    def __init__(self):
        # An empty stack has no top node.
        self.top = None

    # Add a method to add a new node to the top of the stack.
    def push(self, value):
        """Add a new node to the top of the stack."""
        # Keep the previous top linked below the new node.
        self.top = Node(value, self.top)

    # Add a method to remove and return the top value, or raise IndexError if empty.
    def pop(self):
        """Remove and return the top value, or raise IndexError if empty."""
        if self.top is None:
            raise IndexError("Cannot pop from an empty stack.")

        value = self.top.value
        # Moving the top reference removes the first node from the stack.
        self.top = self.top.next_node
        return value

    # Add a method to print the stack from top to bottom without using a compound data type.
    def print_stack(self):
        """Print every value from top to bottom without changing the stack."""
        if self.top is None:
            print("Pila vacía")
            return

        current = self.top
        print("Top", end="")
        # Follow node references without using a compound data type.
        while current is not None:
            print(" -> ", end="")
            print(current.value, end="")
            current = current.next_node
        print(" -> None")


if __name__ == "__main__":
    # Demonstrate that the last value pushed is the first value popped.
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    print("Elminado:", stack.pop())
    stack.print_stack()
