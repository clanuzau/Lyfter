"""
Student: Cesar Lanuza Urbina.  
Program: Python Intermedio - Sort binary tree values using Bubble Sort.
"""


# Define a class to represent a node in the binary tree.
class Node:
    """Store a value and references to at most two child nodes."""

    # Initialize a node with a value and optional references to left and right children.
    def __init__(self, value):
        self.value = value
        # A new node starts without children.
        self.left = None
        self.right = None


# Implement a binary tree with search order insertion and tree printing.
class BinaryTree:
    """Represent a binary tree with values inserted in search order."""

    # Initialize an empty tree with no root node.
    def __init__(self):
        # An empty tree has no root node.
        self.root = None

    # Add a method to insert a new value into the tree, maintaining search order.
    def insert(self, value):
        """Insert a comparable value; duplicate values go to the right."""
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        current = self.root
        # Follow child references until an available position is found.
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

    # Add a method to sort the tree's values using Bubble Sort without modifying the tree.
    def bubble_sort(self):
        """Return values sorted with Bubble Sort without modifying the search tree."""
        values = []
        pending = []
        if self.root is not None:
            pending.append(self.root) # Start with the root node in the pending list.

        # Collect values in preorder rather than using the tree's sorted inorder traversal.
        while pending:
            node = pending.pop() # Remove the last node from the pending list to process it.
            values.append(node.value) # 
            # Push the right child first so the left subtree is visited first.
            if node.right is not None:
                pending.append(node.right)  
            if node.left is not None:
                pending.append(node.left)

        # Each pass moves the largest remaining value to the sorted suffix.
        for end in range(len(values) - 1, 0, -1):
            swapped = False
            for index in range(end):
                if values[index] > values[index + 1]:
                    # Swap adjacent elements that are out of ascending order.
                    values[index], values[index + 1] = values[index + 1], values[index]
                    swapped = True

            # Empty and single-value lists need no passes; ordered lists stop early.
            if not swapped:
                break

        # Sorting a separate list preserves node values and search-order insertion.
        return values

    # Add a method to print the entire tree with labels and indentation for each level.
    def print_tree(self):
        """Print the entire tree with labels and indentation for each level."""
        if self.root is None:
            print("El árbol está vacío.")
            return

        self._print_node(self.root, "", "Raíz")

    # Add a helper method to print a node and its children recursively.
    def _print_node(self, node, indentation, label):
        """Print a node and recursively print both of its child positions."""
        if node is None:
            # Show missing children to make the tree's shape explicit.
            print(f"{indentation}{label}: Vacío")
            return

        # Print the current node's value with its label and indentation.
        print(f"{indentation}{label}: {node.value}")
        # Recursion visits every node without a list, dictionary, or tuple.
        self._print_node(node.left, indentation + "    ", "Izquierdo")
        self._print_node(node.right, indentation + "    ", "Derecho")


if __name__ == "__main__":
    # Build and display an example tree using individual insertions.
    tree = BinaryTree()
    tree.insert(40)
    tree.insert(20)
    tree.insert(60)
    tree.insert(10)
    tree.insert(30)
    tree.insert(50)
    tree.insert(70)
    print("Árbol original:")
    tree.print_tree()
    # Display the sorted values while keeping the original tree intact.
    print("Valores ordenados de menor a mayor con Bubble Sort:", tree.bubble_sort())
