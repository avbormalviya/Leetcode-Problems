
# Problem statement

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Solution


from typing import Optional
import sys


# 🔹 Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Node value
        self.next = next  # Pointer to the next node


# 🔹 Linked List class to create and manage linked lists
class LinkList:
    def __init__(self):
        self.head = None  # Head (first node) of the list
        self.tail = None  # Tail (last node) of the list

    def addNode(self, val):
        """Adds a new node with value `val` to the linked list"""
        newNode = ListNode(val)  # Create a new node

        if self.head:
            # If the list is not empty, add new node to the end
            self.tail.next = newNode  # Point the last node to newNode
            self.tail = newNode  # Update tail to be the newNode
        else:
            # If the list is empty, initialize head and tail
            self.head = newNode
            self.tail = self.head


# 🔹 Solution class for adding two numbers represented as linked lists
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given two non-empty linked lists representing two non-negative integers,
        returns a new linked list representing their sum.
        """
        new_head = ListNode()  # Dummy node to simplify list construction
        new_curr = new_head  # Pointer to the current node in the new list
        carry = 0  # Carry-over value for addition

        # Traverse both lists until both are exhausted and no carry is left
        while l1 or l2 or carry:
            total = carry  # Start with carry from the previous addition

            if l1:
                total += l1.val  # Add l1's current node value
                l1 = l1.next  # Move to the next node

            if l2:
                total += l2.val  # Add l2's current node value
                l2 = l2.next  # Move to the next node

            carry = total // 10  # Compute carry for next iteration
            new_curr.next = ListNode(total % 10)  # Store last digit of sum in a new node
            new_curr = new_curr.next  # Move pointer forward

        return new_head.next  # Return the actual head (skipping the dummy node)


# 🔹 Helper function to convert a list of numbers to a linked list
def list_to_linked_list(arr):
    """
    Converts a list of integers into a linked list and returns its head.
    """
    linked_list = LinkList()  # Create a new linked list object
    for num in arr:
        linked_list.addNode(num)  # Add each number as a node
    return linked_list.head  # Return the head of the linked list


if __name__ == "__main__":
    # Read input as space-separated numbers
    arr1 = list(map(int, sys.stdin.readline().strip().split()))
    arr2 = list(map(int, sys.stdin.readline().strip().split()))

    # Convert lists to Linked Lists
    l1 = list_to_linked_list(arr1)
    l2 = list_to_linked_list(arr2)

    # Solve and Print Output
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    # Print the resulting linked list
    output = []
    while result:
        output.append(str(result.val))  # Collect values in a list
        result = result.next  # Move to the next node

    print(output)  # Print the output
