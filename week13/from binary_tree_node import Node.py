from binary_tree_node import Node


class BinaryTree:
    def __init__(self, val):
        """Create a new tree"""
        self.root = Node(val)

    def __str__(self):
        """Represent tree as a user-friendly string"""
        return "BinTree(" + str(self.root) + ")"

    def __repr__(self):
        """Represent tree as a full string representation"""
        return "BinTree:\n{" + repr(self.root) + "}"

    # The following methods are just a simple, hacky
    # way to populate the tree. They do not yield a
    # balanced or particularly meaningfully
    # structured tree, they simply let us put some data
    # into different positions in the tree. For
    # demonstration purposes only.

    # Populate the leftmost subtree
    def add_val_l(self, val):
        """Add a value to the leftmost binary subtree
        Value -> None"""
        n = Node(val)
        self.add_node_l(self.root, n)

    def add_node_l(self, current_node, new_node):
        """Attach a node to the leftmost binary subtree
        Node Node -> None"""
        if (current_node.left is None):
            current_node.left = new_node
        elif (current_node.right is None):
            current_node.right = new_node
        else:
            self.add_node_l(current_node.left, new_node)

    # Populate the rightmost subtree
    def add_val_r(self, val):
        """Add a value to the leftmost binary subtree
        Value -> None"""
        n = Node(val)
        self.add_node_r(self.root, n)

    def add_node_r(self, current_node, new_node):
        """Attach a node to the rightmost binary subtree
        Node Node -> None"""
        if (current_node.right is None):
            current_node.right = new_node
        elif (current_node.left is None):
            current_node.left = new_node
        else:
            self.add_node_r(current_node.right, new_node)

    # TODO: Write a recursive method to search the
    # tree for a particular value. The "contains"
    # method should return True if the value is to be
    # found anywhere on the tree.
    def contains(self, value):
        """
        Recursively check nodes to see if they match value
        Value -> Boolean
        """
        return self._contains_recursive(self.root, value)
    
    def _contains_recursive(self, node, value):
        "Helper method"
        if node is None:
            return False # Base case: reached the end of a branch
        
        if node.val == value:
            return True # Found the value
        
        return self._contains_recursive(node.left, value) or self._contains_recursive(node.right, value)