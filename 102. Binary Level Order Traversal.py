
# Problem statement

"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
"""


# Solution

from collections import deque  # Import deque for efficient queue operations


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        # If the tree is empty, return an empty list
        if not root:
            return []

        result = []  # List to store level-wise traversal
        queue = deque([root])  # Initialize queue with root node

        while queue:
            level = []  # List to store values of nodes at current level

            # Iterate through all nodes in the current level
            for i in range(len(queue)):
                node = queue.popleft()  # Remove and get the first node in the queue
                level.append(node.val)  # Add node value to the level list

                # Add left child to queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add right child to queue if it exists
                if node.right:
                    queue.append(node.right)

            result.append(level)  # Append current level values to result

        return result  # Return the level-order traversal


# Example usage:
if __name__ == "__main__":
    # Constructing the binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]
