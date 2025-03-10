
# Problem Statement

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# Solution


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find indices of two numbers that add up to the target.
        Uses a dictionary (hash map) to achieve O(n) time complexity.

        :param nums: List of integers
        :param target: Target sum
        :return: Indices of the two numbers that add up to target
        """
        num_map = {}  # Dictionary to store number indices

        # Iterate through the list while storing indices in the dictionary
        for i, num in enumerate(nums):
            complement = target - num  # Find the required number to reach the target

            # If complement is already in the dictionary, return the pair of indices
            if complement in num_map:
                return [num_map[complement], i]

            # Store the index of the current number in the dictionary
            num_map[num] = i

        return []  # Return an empty list if no solution is found


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
