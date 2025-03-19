
# Problem Statement

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


# Solution


from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution class to check if a binary tree is symmetric.
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the given binary tree is symmetric (mirror of itself), else False.
        """

        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            """
            Helper function to check if two trees are mirror images.
            """
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (
                    t1.val == t2.val and
                    is_mirror(t1.left, t2.right) and
                    is_mirror(t1.right, t2.left)
            )

        if root is None:
            return True  # An empty tree is symmetric

        return is_mirror(root.left, root.right)


# Example Usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    solution = Solution()
    print(solution.isSymmetric(root))  # Output: True
