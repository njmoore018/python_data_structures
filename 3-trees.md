# Trees Introduction
![Tree](/images/tree.jpg)
A tree is a data structure consisting of nodes connected by edges. Each node in a tree can have multiple child nodes but has only one parent node, except for the root node which has no parent. Trees are used to represent hierarchical structures, such as the file system of a computer or the structure of a company and can be created in Python by using classes.
Here's an example of a tree class:
```python
# Tree Class
class Tree:
    # Node class since a tree must be made of nodes
    class Node:
        def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __init__(self):
        root = None
```

### Commonly Used Terms
- `Node`: A single unit of data that contains a value and one or more child nodes.

- `Root`: The topmost node in a tree. It has no parent nodes.

- `Parent`: A node that has one or more child nodes.

- `Child`: A node that has a parent node.

- `Leaf`: A node that has no children.

- `Branch`: A non-leaf node.

- `Level`: The distance between a node and the root node, where the root node is at level 0.

## Common Functions and Performance
- `Insert`: Add a node to the tree. The efficiency of this operation depends on the implementation of the tree but is generally O(log n) for a balanced tree and O(n) for an unbalanced tree.

- `Remove`: Remove a node from the tree. This operation has an efficiency of O(log n) in a balanced tree, where n is the number of nodes in the tree.

- `Traverse Forward`: Traverse the tree in ascending order. This operation has an efficiency of O(n), where n is the number of nodes in the tree.

- `Traverse Backward`: Traverse the tree in descending order. This operation has an efficiency of O(n), where n is the number of nodes in the tree.

- `Membership`: Check if a value is present in the tree. This operation has an efficiency of O(log n) in a balanced tree, where n is the number of nodes in the tree.

- `Search`: Find a node in the tree. The efficiency of this operation depends on the implementation of the tree but is generally O(log n) for a balanced tree and O(n) for an unbalanced tree.

- `Find Height`: Determine the height of the tree. This operation has an efficiency of O(n), where n is the number of nodes in the tree.

- `Size`: Find the number of nodes in the tree. The efficiency of this operation depends on the implementation of the tree but is generally O(n).

## Applications
![Company Meeting](/images/company_meeting.jpg)
Trees can be used in a wide variety of applications. Some examples include:

- `File Systems`: In a file system, directories and files can be represented using a tree structure, where the root node represents the top-level directory, and each child node represents a subdirectory or file within that directory.

- `Organization Charts`: In an organization, the hierarchy of employees can be represented using a tree structure, where the root node represents the CEO, and each child node represents a manager or employee within the organization.

- `Decision Trees`: In machine learning, decision trees can be used to represent a sequence of decisions that lead to a particular outcome. Each node in the tree represents a decision, and the branches represent the possible outcomes of that decision.

## Example
Given a binary tree, determine if it is a valid binary search tree (BST).

A BST is a binary tree where the left subtree of a node contains only nodes with values less than the node's value, and the right subtree of a node contains only nodes with values greater than the node's value. Also, each left and right subtree must also be a valid BST.

For example, the following binary tree is a valid BST:
```markdown
    5
   / \
  3   7
 / \   \
2   4   8
```

But the following binary tree is not a valid BST:
```markdown
    5
   / \
  3   7
 / \   \
2   8   4
```

Using our tree class from earlier, we will traverse over each node by using recursion and verify that the left value is less than the current value and the right value is greater. If we find an instance where this is not true, then the tree is not valid.
```python
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

    def is_valid_tree(self):
        if self.root is None:
            return True
        else:
            if root.left is not None:
                if root.left.value > root.value:
                    return False
                else:
                    return _is_valid_tree(root.left)
            if root.right is not None:
                if root.right.value < root.value:
                    return False
                else:
                    return _is_valid_tree(root.right)

    def _is_valid_tree(self, node):
        if node.right is not None:
            if node.right.value < node.value:
                    return False
                else:
                    return _is_valid_tree(node.right)
        if node.left is not None:
            if node.left.value < node.value:
                    return False
                else:
                    return _is_valid_tree(node.left)
        return True
```

## Problem
Suppose you are given a binary search tree and you want to find the nth smallest element in the tree. Write a Python function that takes an integer n, and returns the nth smallest element in the tree. Assume the tree is a valid binary tree.

For example, suppose you have the following binary search tree:
```markdown
    5
   / \
  3   7
 / \   \
2   4   8
```

If n=3, the function should return 4, since 4 is the third smallest element in the tree. If n=5, the function should return 7, since 7 is the fifth smallest element in the tree.

`Hint`: If you perform an inorder traversal of the tree, which will visit the elements in ascending order, you need only keep track of the current position in the traversal and return the nth element when you reach it.

This code is provided for you:
```Python
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
        pass # Your code should go here

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
```

[View Solution](solutions/3-trees.py)

[Back to Welcome Page](0-welcome.md)