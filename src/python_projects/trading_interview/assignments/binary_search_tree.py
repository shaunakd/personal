"""
Project 23: Binary Search Tree (BST)

You're tasked with implementing various operations on a binary search tree (BST).
The BST will store integers, and you need to implement methods for insertion, deletion, and finding the minimum and maximum values.

class BinarySearchTree:
    def __init__(self):
        pass

    def insert(self, value: int):
        pass

    def delete(self, value: int):
        pass

    def find_min(self) -> int:
        pass

    def find_max(self) -> int:
        pass

Methods
insert(value: int): Inserts a new node with the given integer value into the BST.
delete(value: int): Deletes a node with the given integer value from the BST. If the value doesn't exist, do nothing.
find_min() -> int: Returns the minimum integer value stored in the BST.
find_max() -> int: Returns the maximum integer value stored in the BST.
"""

from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        return node

    def delete(self, value: int):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min_node(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def find_min(self) -> Optional[int]:
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self) -> Optional[int]:
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
