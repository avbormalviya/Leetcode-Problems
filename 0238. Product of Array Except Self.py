
# Problem Statement

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


# Solution


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n  # Initialize result array with 1s

        # First pass: calculate prefix product for each index
        prefix = 1
        for i in range(n):
            res[i] = prefix        # Store the product of all elements to the left of i
            prefix *= nums[i]      # Update prefix for next index

        # Second pass: calculate suffix product and multiply it with prefix product in res
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix       # Multiply with the product of all elements to the right of i
            suffix *= nums[i]      # Update suffix for next index to the left

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
