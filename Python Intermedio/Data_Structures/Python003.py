"""
Student: Cesar Lanuza Urbina.  
Program: Pyton Intermedio - Implement a binary tree with search order insertion and tree printing.
"""


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

    # Add a method to print the entire tree with labels and indentation for each level.
    def print_tree(self):
        """Print the entire tree with labels and indentation for each level."""
        if self.root is None:
            print("El árbol esta vacío.")
            return

        self._print_node(self.root, "", "Raíz")

    # Add a helper method to print a node and its children recursively.
    def _print_node(self, node, indentation, label):
        """Print a node and recursively print both of its child positions."""
        if node is None:
            # Show missing children to make the tree's shape explicit.
            print(f"{indentation}{label}: None")
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
    tree.print_tree()
