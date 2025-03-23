
# Problem Statement

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

Return k.
"""

# Solution


from collections import defaultdict


class Solution:
    def removeElement(self, nums, val):
        i = 0  # Pointer for valid elements

        for j in range(len(nums)):  # Iterate through the array
            if nums[j] != val:  # If current element is not val, keep it
                nums[i] = nums[j]  # Move it to index i
                i += 1  # Increment valid element count

        return i  # New length of modified array


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    # Create an instance of the Solution class
    sol = Solution()

    # Call the removeElement method and store the result
    result = sol.removeElement(nums, val)

    # Print the result
    print(result)
