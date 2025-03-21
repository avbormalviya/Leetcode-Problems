
# Problem Statement

"""
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


# Solution


class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Dictionary to store {needed_value: index}

        for index, num in enumerate(nums):
            if num in seen:
                return [seen[num], index]

            seen[target - num] = index  # Store needed value to form target

        return []


# Input handling
if __name__ == "__main__":
    # Taking space-separated integers as input for the array
    nums = list(map(int, input().split()))

    # Taking target sum as input
    target = int(input())

    # Creating an instance of Solution class
    sol = Solution()

    # Calling the twoSum function and printing the result
    ans = sol.twoSum(nums, target)
    print(ans)  # Output the indices of the two numbers
