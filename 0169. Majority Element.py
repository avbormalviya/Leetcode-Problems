
# Problem Statement

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""


# Solution


class Solution:
    def majorityElement(self, nums):
        # Existing logic to find the candidate
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Verify the candidate
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        return -1  # Or handle the case where no majority exists


if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()
    result = sol.majorityElement(nums)
    print(result)
