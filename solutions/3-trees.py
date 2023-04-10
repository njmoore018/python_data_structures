# Tree Class
class Tree:
    # Node class since a tree must be made of nodes
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Insert 'value' into the Tree.  If the Tree
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = Tree.Node(value)
        else:
            self._insert(value, self.root)  # Start at the root

    def _insert(self, value, node):
        """
        This function will look for a place to insert a node
        with 'value' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        # Prevent duplicate values from being included in the Tree.
        if value == node.value:
            return
        elif value < node.value:
            # The value belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = Tree.Node(value)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(value, node.left)
        else:
            # The value belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = Tree.Node(value)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(value, node.right)

    def get_nth_smallest_value(self, n):
        stack = []
        count = 0
        current = self.root
    
        while count < n:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                count += 1
                if count == n:
                    return current.value
                current = current.right
            else:
                return None

def main():
    tree = Tree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    print(tree.get_nth_smallest_value(1))   # Expected output of 2
    print(tree.get_nth_smallest_value(2))   # Expected output of 3
    print(tree.get_nth_smallest_value(3))   # Expected output of 4
    print(tree.get_nth_smallest_value(4))   # Expected output of 5
    print(tree.get_nth_smallest_value(5))   # Expected output of 7
    print(tree.get_nth_smallest_value(6))   # Expected output of 8
    print(tree.get_nth_smallest_value(7))   # Expected output of None

if __name__ == "__main__":
    main()